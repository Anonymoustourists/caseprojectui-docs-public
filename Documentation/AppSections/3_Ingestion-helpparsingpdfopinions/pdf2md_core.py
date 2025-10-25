#!/usr/bin/env python3
"""
Michigan Court of Appeals PDF to Markdown Converter
Core "dumb" pattern recognition system extracted from MiCase project

This is the rule-based conversion system that works without AI/LLMs.
It uses pattern recognition to identify and format Michigan court opinions.
"""

import re
import json
from pathlib import Path
from typing import List, Tuple, Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF (fitz) not installed. Run: pip install PyMuPDF")
    raise

try:
    import regex
except ImportError:
    print("ERROR: regex module not installed. Run: pip install regex")
    raise

# ===============================================
# PATTERN RECOGNITION RULES
# ===============================================

# Boilerplate patterns to remove from Michigan Court of Appeals PDFs
COA_BOILERPLATE_PATTERNS = [
    # Normal and "spaced-letter" variants:
    r"^\s*STATE\s+OF\s+MICHIGAN\s*$",
    r"^\s*S\s*T\s*A\s*T\s*E\s+O\s*F\s+M\s*I\s*C\s*H\s*I\s*G\s*A\s*N\s*$",
    r"^\s*COURT\s+OF\s+APPEALS\s*$",
    r"^\s*C\s*O\s*U\s*R\s*T\s+O\s*F\s*A\s*P\s*P\s*E\s*A\s*L\s*S\s*$",
    r"^\s*-\d+-\s*$",  # Page numbers like "-3-"
    r"If this opinion indicates that it is ['']FOR PUBLICATION[''].*$",
    r"^UNPUBLISHED\b.*$",
    r"^PUBLISHED\b.*$",
    r"^No\.\s*\d+\b.*$",  # Case numbers
    r"^LC\s*No\.\s*\S+.*$",  # Lower court numbers
    r"^\d{1,2}:\d{2}\s*(AM|PM)\s*$",  # Timestamps
]

BOILERPLATE_RE = regex.compile("|".join(f"({p})" for p in COA_BOILERPLATE_PATTERNS), regex.IGNORECASE)

# Heading mappers - convert court outline format to Markdown
HEADING_REPLACERS = [
    # Map leading tokens to markdown levels, keep the token text.
    (regex.compile(r"^(I{1,6})\.(\s+)(.+)$"), r"# \1. \3"),        # I., II., III. -> #
    (regex.compile(r"^([A-Z])\.(\s+)(.+)$"), r"## \1. \3"),         # A., B., C. -> ##
    (regex.compile(r"^(\d{1,2})\.(\s+)(.+)$"), r"### \1. \3"),      # 1., 2., 3. -> ###
    (regex.compile(r"^([ivxlcdm]{1,6})\.(\s+)(.+)$", regex.IGNORECASE), r"#### \1. \3"),  # i., ii., iii. -> ####
]

# Legal abbreviations that should NOT end sentences
ABBR_TOKENS = {"MCL.", "MRE.", "U.S.", "Inc.", "Co.", "Ct.", "App.", "No.", "v.", "Ltd.", "L.L.C.", "L.L.P."}

# Footnote definition pattern
FOOTNOTE_DEF_RE = regex.compile(r"^(\d{1,3})[\).]\s+(.*)$")

# Sentence ending patterns
SENT_END_RE = regex.compile(r"([\.!?]|\]\))\s*$")
ABBR_RE = regex.compile(r"(MCL\.|MRE\.|U\.S\.|Inc\.|Co\.|Ct\.|App\.|No\.|v\.|Ltd\.|L\.L\.C\.|L\.L\.P\.)$")

# ===============================================
# PDF TEXT EXTRACTION
# ===============================================

def extract_pdf_text_with_blocks(pdf_path: Path) -> List[str]:
    """
    Extract text from PDF using PyMuPDF block-based extraction.
    This preserves layout better than simple text extraction.
    
    Returns:
        List of strings, one per page
    """
    doc = fitz.open(str(pdf_path))
    pages: List[str] = []
    
    for page in doc:
        # Get text blocks (preserves layout)
        blocks = page.get_text("blocks")
        
        # Sort blocks by position (top to bottom, left to right)
        blocks_sorted = sorted(blocks, key=lambda b: (round(b[1], 1), round(b[0], 1)))
        
        texts = []
        for b in blocks_sorted:
            block_text = b[4]  # Text content is at index 4
            if not block_text:
                continue
            
            # Normalize line endings
            block_text = block_text.replace("\r\n", "\n").replace("\r", "\n")
            texts.append(block_text.strip("\n"))
        
        # Join blocks with double newlines
        page_text = "\n\n".join(texts)
        pages.append(page_text)
    
    doc.close()
    return pages

# ===============================================
# CLEANING AND BOILERPLATE REMOVAL
# ===============================================

def strip_boilerplate(line: str) -> bool:
    """Check if a line matches boilerplate patterns that should be removed."""
    return bool(BOILERPLATE_RE.search(line))

# Patterns that indicate the start of the actual opinion body
CAPTION_END_HINTS = [
    regex.compile(r"^PER\s+CURIAM\.\s*$", regex.IGNORECASE),
    regex.compile(r"^OPINION\b", regex.IGNORECASE),
]

def find_body_start(lines: List[str]) -> int:
    """
    Find where the actual opinion body starts (after caption/metadata).
    
    Returns:
        Index of the first line of the opinion body
    """
    # Look for explicit markers like "PER CURIAM." or "OPINION"
    for i, ln in enumerate(lines):
        for pat in CAPTION_END_HINTS:
            if pat.search(ln.strip()):
                return i
    
    # Fallback: look for first heading pattern
    for i, ln in enumerate(lines):
        if regex.match(r"^(I{1,6}|[A-Z]|\d+|[ivxlcdm]+)\.\s.*$", ln.strip()):
            return i
    
    return 0

# ===============================================
# HEADING MAPPING
# ===============================================

def map_headings(lines: List[str]) -> List[str]:
    """
    Convert court outline headings to Markdown format.
    
    Examples:
        "I. BACKGROUND" -> "# I. BACKGROUND"
        "A. The Trial" -> "## A. The Trial"
        "1. Evidence" -> "### 1. Evidence"
        "i. Testimony" -> "#### i. Testimony"
    """
    out = []
    for ln in lines:
        s = ln.rstrip()
        replaced = False
        
        # Try each heading pattern
        for rx, repl in HEADING_REPLACERS:
            m = rx.match(s)
            if m:
                out.append(rx.sub(repl, s))
                replaced = True
                break
        
        if not replaced:
            out.append(s)
    
    return out

# ===============================================
# PARAGRAPH JOINING
# ===============================================

def join_lines_to_paragraphs(lines: List[str]) -> List[str]:
    """
    Join wrapped lines into proper paragraphs while preserving structure.
    
    This is the "smart" part that handles:
    - Hyphenated words broken across lines
    - Legal abbreviations that shouldn't end sentences
    - Proper paragraph breaks
    """
    paras: List[str] = []
    buf: List[str] = []

    def flush():
        """Flush current buffer to a paragraph."""
        if not buf:
            return
        text = " ".join(x.strip() for x in buf)
        
        # Fix hyphenated words broken across lines
        text = regex.sub(r"(\w)-\s+(\w)", r"\1\2", text)
        
        paras.append(text)
        buf.clear()

    for ln in lines:
        st = ln.rstrip()
        
        # Empty line = paragraph break
        if not st.strip():
            flush()
            continue
        
        # Markdown heading = paragraph break
        if st.startswith("# "):
            flush()
            paras.append(st)
            continue
        
        # First line in buffer
        if not buf:
            buf.append(st)
            continue
        
        # Check if previous line ended a sentence (but not with abbreviation)
        if SENT_END_RE.search(buf[-1]) and not ABBR_RE.search(buf[-1]):
            flush()
            buf.append(st)
        else:
            buf.append(st)

    flush()
    return paras

# ===============================================
# FOOTNOTE PROCESSING
# ===============================================

def split_body_and_footnotes(paras: List[str]) -> Tuple[List[str], List[Tuple[str, str]]]:
    """
    Separate main body from footnote definitions.
    
    Returns:
        Tuple of (body_paragraphs, footnotes_list)
        footnotes_list contains (number, text) tuples
    """
    body, fns = [], []
    
    for p in paras:
        m = FOOTNOTE_DEF_RE.match(p.strip())
        if m and len(p.split()) > 3:  # Must have substantial content
            num = m.group(1)
            text = m.group(2).strip()
            fns.append((num, text))
        else:
            body.append(p)
    
    # Remove duplicates while preserving order
    seen = {}
    ordered = []
    for n, t in fns:
        if n not in seen:
            seen[n] = t
            ordered.append((n, t))
    
    return body, ordered

# ===============================================
# METADATA EXTRACTION
# ===============================================

# Month names for date extraction
MONTHS = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)
MONTH_PATTERN = r"(?:%s)\s+\d{1,2},\s+\d{4}" % "|".join(MONTHS)

# Metadata extraction patterns
META_PATTERNS = {
    "case_no": regex.compile(r"\bNo\.\s*(\d{3,})\b", regex.IGNORECASE),
    "lc_no":   regex.compile(r"\bLC\s*No\.\s*([A-Za-z0-9\-]+)", regex.IGNORECASE),
    "judges":  regex.compile(r"^Before:\s*(.+)$", regex.IGNORECASE|regex.MULTILINE),
    "date":    regex.compile(MONTH_PATTERN),
    "pub":     regex.compile(r"\b(UNPUBLISHED|FOR\s+PUBLICATION)\b", regex.IGNORECASE),
    "lower_court": regex.compile(r"\b([A-Z][a-z]+ County Circuit Court)\b"),
}

def _normalize_spaces(s: str) -> str:
    """Normalize whitespace in a string."""
    return regex.sub(r"\s+", " ", s).strip()

def extract_case_name_from_banner(first_page: str) -> Optional[str]:
    """
    Extract case name from PDF banner (common in MCOA PDFs).
    
    Example banner:
    'COA 369250 CORE VALUES CONSTRUCTION LLC V SHEEHAN'S ON THE GREEN INC Opinion - Authored - Published 7/9/2025'
    """
    m = regex.search(r"\bCOA\s+\d+\s+(.+?)\s+Opinion\b", first_page, regex.IGNORECASE)
    if not m:
        return None
    
    chunk = m.group(1)
    # Normalize ' V ' to ' v '
    chunk = regex.sub(r"\s+V\s+", " v ", chunk, flags=regex.IGNORECASE)
    return _normalize_spaces(chunk)

def extract_meta_from_pages(pages: List[str]) -> dict:
    """
    Extract metadata from the first page of the PDF.
    
    Returns:
        Dictionary with case metadata
    """
    meta: dict = {
        "case_name": None,
        "case_no": None,
        "lc_no": None,
        "judges": None,
        "date": None,
        "publication": None,
        "lower_court": None,
        "source": "pdf2md_core.py",
    }
    
    if not pages:
        return meta

    first = pages[0]
    flat = _normalize_spaces(first)

    # Extract case name from banner first
    case_name = extract_case_name_from_banner(first)
    if not case_name:
        # Try from caption: look for plaintiff v defendant pattern
        cap = "\n".join(first.splitlines()[:120])
        cap_norm = _normalize_spaces(cap)
        mcap = regex.search(r"([A-Z0-9\.''\-,& ]+\s+v\s+[A-Z0-9\.''\-,& ]+)", cap_norm)
        if mcap:
            case_name = _normalize_spaces(mcap.group(1))
    
    meta["case_name"] = case_name

    # Extract other metadata fields
    for key, rx in META_PATTERNS.items():
        m = rx.search(first) or rx.search(flat)
        if m:
            val = m.group(1) if m.lastindex else m.group(0)
            if key == "pub":
                val = "PUBLISHED" if "PUBLICATION" in val.upper() else "UNPUBLISHED"
                meta["publication"] = val
            elif key == "judges":
                meta["judges"] = _normalize_spaces(val)
            else:
                meta[key if key != "pub" else "publication"] = _normalize_spaces(val)

    # Set court type
    meta.setdefault("court", "Michigan Court of Appeals")
    return meta

def write_meta_json(meta: dict, md_path: Path) -> Optional[Path]:
    """Write metadata to a .meta.json file alongside the markdown."""
    try:
        out = md_path.with_suffix("")  # Remove .md extension
        meta_path = out.with_name(out.name + ".meta.json")
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        return meta_path
    except Exception:
        return None

# ===============================================
# MAIN CONVERSION FUNCTION
# ===============================================

def convert_pdf_to_markdown(
    pdf_path: Path,
    output_dir: Path,
    inline_footnotes: bool = False
) -> Tuple[bool, Optional[Path], Optional[Path]]:
    """
    Convert a Michigan Court of Appeals PDF to Markdown using rule-based patterns.
    
    Args:
        pdf_path: Path to input PDF file
        output_dir: Directory to write output files
        inline_footnotes: Whether to convert footnotes inline (default: False)
        
    Returns:
        Tuple of (success: bool, markdown_path: Optional[Path], metadata_path: Optional[Path])
    """
    try:
        # Extract text from PDF
        pages = extract_pdf_text_with_blocks(pdf_path)
        
        # Extract metadata before cleaning
        meta = extract_meta_from_pages(pages)
        
        # Clean boilerplate from each page
        cleaned_pages: List[str] = []
        for pg in pages:
            lines = [ln for ln in pg.splitlines() if not strip_boilerplate(ln.strip())]
            cleaned_pages.append("\n".join(lines).strip())
        
        # Join all pages
        raw_joined = ("\n\n---PAGE---\n\n").join([p for p in cleaned_pages if p])
        
        # Find opinion body (skip caption/metadata)
        all_lines = raw_joined.splitlines()
        while all_lines and not all_lines[0].strip():
            all_lines.pop(0)
        
        body_start = find_body_start(all_lines)
        body_lines = all_lines[body_start:]
        
        # Apply rule-based formatting
        body_lines = map_headings(body_lines)
        paras = join_lines_to_paragraphs(body_lines)
        paras, footnotes = split_body_and_footnotes(paras)
        
        # Build final markdown
        parts: List[str] = []
        for p in paras:
            parts.append(p)
            parts.append("")  # Add blank line after each paragraph
        
        # Add footnotes section if any found
        if footnotes:
            parts.append("---")
            parts.append("")
            parts.append("## Footnotes")
            parts.append("")
            for n, t in footnotes:
                parts.append(f"[^{n}]: {t}")
        
        md = "\n".join(parts).rstrip() + "\n"
        
        # Optional inline footnote conversion
        if inline_footnotes and md is not None:
            def repl(m: regex.Match) -> str:
                word = m.group(1)
                num = m.group(2)
                prev = word.split()[-1]
                # Skip if previous word is likely not a footnote reference
                if prev in {"No.", "MCL", "US", "U.S.", "NW2d", "N\u2019d", "Mich", "WL"}:
                    return m.group(0)
                return f"{word}[^{num}]"
            md = regex.sub(r"(\w)(\d{1,3})(?![\d\w])", repl, md)
        
        # Write output files
        output_dir.mkdir(parents=True, exist_ok=True)
        out_path = output_dir / (pdf_path.stem + ".md")
        out_path.write_text(md, encoding="utf-8")
        
        # Write metadata sidecar
        meta_path = write_meta_json(meta, out_path)
        
        return True, out_path, meta_path
        
    except Exception as e:
        print(f"ERROR: PDF conversion failed: {e}")
        return False, None, None

# ===============================================
# COMMAND LINE INTERFACE
# ===============================================

def main():
    """Simple command line interface for testing."""
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python pdf2md_core.py <pdf_path> <output_dir>")
        print("       Convert a Michigan Court of Appeals PDF to Markdown")
        sys.exit(1)
    
    pdf_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    
    if not pdf_path.exists():
        print(f"ERROR: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    success, md_path, meta_path = convert_pdf_to_markdown(pdf_path, output_dir)
    
    if success:
        print(f"SUCCESS: Converted to {md_path}")
        if meta_path:
            print(f"Metadata: {meta_path}")
    else:
        print("FAILED: Conversion failed")
        sys.exit(1)

if __name__ == "__main__":
    main()