<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Michigan Court PDF to Markdown Converter - Implementation Guide](#michigan-court-pdf-to-markdown-converter---implementation-guide)
  - [What's Included](#whats-included)
    - [Core Scripts](#core-scripts)
  - [How It Works](#how-it-works)
    - [1. PDF Text Extraction](#1-pdf-text-extraction)
    - [2. Boilerplate Recognition and Removal](#2-boilerplate-recognition-and-removal)
    - [3. Heading Structure Detection](#3-heading-structure-detection)
    - [4. Smart Paragraph Joining](#4-smart-paragraph-joining)
    - [5. Footnote Processing](#5-footnote-processing)
    - [6. Metadata Extraction](#6-metadata-extraction)
  - [Implementation for Your System](#implementation-for-your-system)
    - [Step 1: Install Dependencies](#step-1-install-dependencies)
    - [Step 2: Basic Usage](#step-2-basic-usage)
    - [Step 3: Batch Processing](#step-3-batch-processing)
  - [Customization Options](#customization-options)
    - [Modifying Boilerplate Patterns](#modifying-boilerplate-patterns)
    - [Adjusting Heading Recognition](#adjusting-heading-recognition)
    - [Adding Legal Abbreviations](#adding-legal-abbreviations)
  - [Integration Patterns](#integration-patterns)
    - [Web Service Integration](#web-service-integration)
    - [Command Line Tool](#command-line-tool)
  - [Performance Notes](#performance-notes)
  - [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
    - [Testing Your Implementation](#testing-your-implementation)
  - [Why This System Works](#why-this-system-works)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Michigan Court PDF to Markdown Converter - Implementation Guide

This directory contains the core "dumb" pattern recognition system extracted from the MiCase project for converting Michigan Court of Appeals and Supreme Court PDFs to Markdown format. This system works entirely through rule-based pattern matching and does NOT require AI/LLM services.

## What's Included

### Core Scripts

- **`pdf2md_core.py`** - Main conversion engine with all pattern recognition logic
- **`requirements_minimal.txt`** - Minimal dependencies needed for the converter
- **`conversion_spec.md`** - Documentation of the conversion rules and patterns
- **`test_converter.py`** - Simple test script to validate the conversion

## How It Works

The "dumb" system is actually quite sophisticated in its pattern recognition:

### 1. PDF Text Extraction

- Uses PyMuPDF (fitz) for block-based text extraction
- Preserves document layout better than simple text extraction
- Sorts text blocks by position (top-to-bottom, left-to-right)

### 2. Boilerplate Recognition and Removal

The system automatically identifies and removes common Michigan court boilerplate:

- "STATE OF MICHIGAN" / "COURT OF APPEALS" headers
- Page numbers (e.g., "-3-")
- Publication disclaimers
- Case number lines
- Timestamps

### 3. Heading Structure Detection

Converts court outline format to Markdown headings:

- `I., II., III.` → `# I. Title` (H1)
- `A., B., C.` → `## A. Title` (H2)  
- `1., 2., 3.` → `### 1. Title` (H3)
- `i., ii., iii.` → `#### i. Title` (H4)

### 4. Smart Paragraph Joining

The system intelligently reconstructs paragraphs by:

- Joining lines that were wrapped in the PDF
- Fixing hyphenated words broken across lines
- Recognizing legal abbreviations that shouldn't end sentences
- Preserving intentional paragraph breaks

### 5. Footnote Processing

- Identifies footnote definitions (numbered lines at page bottoms)
- Separates footnotes from main body text
- Optionally converts inline footnote references to Markdown format

### 6. Metadata Extraction

Automatically extracts case metadata:

- Case name (plaintiff v defendant)
- Case numbers and lower court numbers
- Judge panel information
- Decision date
- Publication status

## Implementation for Your System

### Step 1: Install Dependencies

```bash
pip install PyMuPDF regex pathlib
```

The minimal requirements are:

- **PyMuPDF** (`fitz`) - PDF text extraction
- **regex** - Enhanced regular expressions (better than built-in `re`)
- **pathlib** - File path handling (usually built-in)

### Step 2: Basic Usage

```python
from pathlib import Path
from pdf2md_core import convert_pdf_to_markdown

# Convert a single PDF
pdf_path = Path("opinion.pdf")
output_dir = Path("output")

success, md_path, meta_path = convert_pdf_to_markdown(
    pdf_path=pdf_path,
    output_dir=output_dir,
    inline_footnotes=False  # Set to True to convert footnote numbers
)

if success:
    print(f"Converted to: {md_path}")
    if meta_path:
        print(f"Metadata saved to: {meta_path}")
else:
    print("Conversion failed")
```

### Step 3: Batch Processing

```python
from pathlib import Path
from pdf2md_core import convert_pdf_to_markdown

def convert_directory(input_dir: Path, output_dir: Path):
    """Convert all PDFs in a directory."""
    pdf_files = list(input_dir.glob("*.pdf"))
    
    for pdf_file in pdf_files:
        print(f"Converting {pdf_file.name}...")
        success, md_path, meta_path = convert_pdf_to_markdown(
            pdf_path=pdf_file,
            output_dir=output_dir
        )
        
        if success:
            print(f"✅ {pdf_file.name} -> {md_path.name}")
        else:
            print(f"❌ Failed: {pdf_file.name}")

# Usage
input_directory = Path("input_pdfs")
output_directory = Path("output_markdown")
convert_directory(input_directory, output_directory)
```

## Customization Options

### Modifying Boilerplate Patterns

Edit the `COA_BOILERPLATE_PATTERNS` list in `pdf2md_core.py` to add/remove patterns:

```python
COA_BOILERPLATE_PATTERNS = [
    r"^\s*YOUR_COURT_NAME\s*$",        # Add your court's header
    r"^\s*CUSTOM_PATTERN\s*$",         # Add custom patterns
    # ... existing patterns
]
```

### Adjusting Heading Recognition

Modify `HEADING_REPLACERS` to match your court's outline format:

```python
HEADING_REPLACERS = [
    (regex.compile(r"^(PART\s+[A-Z])\.(\s+)(.+)$"), r"# \1. \3"),  # Custom format
    # ... existing patterns
]
```

### Adding Legal Abbreviations

Extend `ABBR_TOKENS` with abbreviations specific to your jurisdiction:

```python
ABBR_TOKENS = {
    "MCL.", "MRE.", "U.S.",  # Existing
    "CUSTOM.", "ABBR.",      # Add your abbreviations
    # ...
}
```

## Integration Patterns

### Web Service Integration

```python
from flask import Flask, request, jsonify
from pdf2md_core import convert_pdf_to_markdown
import tempfile
from pathlib import Path

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No PDF file provided'}), 400
    
    pdf_file = request.files['pdf']
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir = Path(temp_dir)
        pdf_path = temp_dir / pdf_file.filename
        pdf_file.save(pdf_path)
        
        success, md_path, meta_path = convert_pdf_to_markdown(
            pdf_path=pdf_path,
            output_dir=temp_dir
        )
        
        if success:
            markdown_text = md_path.read_text(encoding='utf-8')
            metadata = {}
            if meta_path:
                import json
                metadata = json.loads(meta_path.read_text(encoding='utf-8'))
            
            return jsonify({
                'success': True,
                'markdown': markdown_text,
                'metadata': metadata
            })
        else:
            return jsonify({'error': 'Conversion failed'}), 500
```

### Command Line Tool

```python
#!/usr/bin/env python3
import argparse
from pathlib import Path
from pdf2md_core import convert_pdf_to_markdown

def main():
    parser = argparse.ArgumentParser(description='Convert Michigan court PDFs to Markdown')
    parser.add_argument('input', help='PDF file or directory')
    parser.add_argument('output', help='Output directory')
    parser.add_argument('--inline-footnotes', action='store_true', 
                       help='Convert footnote numbers to inline format')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if input_path.is_file():
        # Single file
        success, md_path, meta_path = convert_pdf_to_markdown(
            input_path, output_path, args.inline_footnotes
        )
        if success:
            print(f"Converted: {md_path}")
        else:
            print("Conversion failed")
    
    elif input_path.is_dir():
        # Directory of files
        for pdf_file in input_path.glob("*.pdf"):
            success, md_path, meta_path = convert_pdf_to_markdown(
                pdf_file, output_path, args.inline_footnotes
            )
            if success:
                print(f"✅ {pdf_file.name}")
            else:
                print(f"❌ {pdf_file.name}")

if __name__ == '__main__':
    main()
```

## Performance Notes

- **Memory Usage**: The system loads entire PDFs into memory. For very large files (>100MB), consider processing in chunks or streaming.
- **Speed**: Rule-based conversion is very fast - typically 1-5 seconds per document.
- **Accuracy**: The pattern recognition works best with consistently formatted court documents. You may need to adjust patterns for different courts or document types.

## Troubleshooting

### Common Issues

1. **Missing Dependencies**

   ```bash
   pip install PyMuPDF regex
   ```

2. **Text Extraction Fails**
   - Check if PDF is text-based (not scanned image)
   - Try different PyMuPDF extraction methods

3. **Poor Formatting**
   - Adjust boilerplate patterns for your specific court
   - Modify heading recognition patterns
   - Check paragraph joining logic

4. **Missing Metadata**
   - Verify metadata patterns match your court's format
   - Check first page of PDF for expected fields

### Testing Your Implementation

Use the included `test_converter.py` to validate conversions:

```python
from pdf2md_core import convert_pdf_to_markdown
from pathlib import Path

# Test with a sample PDF
test_pdf = Path("sample_opinion.pdf")
output_dir = Path("test_output")

success, md_path, meta_path = convert_pdf_to_markdown(test_pdf, output_dir)

if success:
    print("✅ Conversion successful")
    print(f"Markdown: {md_path}")
    print(f"Metadata: {meta_path}")
    
    # Check output quality
    md_text = md_path.read_text()
    print(f"Length: {len(md_text)} characters")
    print(f"Paragraphs: {md_text.count('\\n\\n')}")
    print(f"Headings: {md_text.count('#')}")
else:
    print("❌ Conversion failed")
```

## Why This System Works

The "dumb" pattern recognition system is highly effective for legal documents because:

1. **Consistent Formatting**: Court documents follow standardized formats
2. **Predictable Structure**: Legal writing uses consistent outline patterns  
3. **Recognizable Boilerplate**: Courts use the same headers/footers repeatedly
4. **Rule-Based Reliability**: No AI "hallucination" or unpredictable behavior
5. **Fast Processing**: No network calls or model loading delays
6. **Offline Operation**: Works completely offline with no external dependencies

The system has been battle-tested on thousands of Michigan court documents and maintains high accuracy while being completely deterministic and debuggable.
