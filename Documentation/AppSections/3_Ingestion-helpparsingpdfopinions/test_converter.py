#!/usr/bin/env python3
"""
Test script for the Michigan Court PDF to Markdown converter.
This script validates that the conversion system works correctly.
"""

import sys
from pathlib import Path
import tempfile
import json

# Add the current directory to path so we can import pdf2md_core
sys.path.insert(0, str(Path(__file__).parent))

try:
    from pdf2md_core import convert_pdf_to_markdown, extract_pdf_text_with_blocks
    print("✅ Successfully imported pdf2md_core")
except ImportError as e:
    print(f"❌ Failed to import pdf2md_core: {e}")
    print("Make sure PyMuPDF and regex are installed:")
    print("pip install PyMuPDF regex")
    sys.exit(1)

def test_basic_functionality():
    """Test the basic functions without requiring a PDF file."""
    print("\n🧪 Testing basic functionality...")
    
    # Test pattern matching
    from pdf2md_core import strip_boilerplate, map_headings, join_lines_to_paragraphs
    
    # Test boilerplate removal
    test_lines = [
        "STATE OF MICHIGAN",
        "COURT OF APPEALS", 
        "This is actual content",
        "-3-",
        "More real content"
    ]
    
    filtered = [line for line in test_lines if not strip_boilerplate(line)]
    expected = ["This is actual content", "More real content"]
    
    if filtered == expected:
        print("✅ Boilerplate removal works correctly")
    else:
        print(f"❌ Boilerplate removal failed. Got: {filtered}, Expected: {expected}")
    
    # Test heading mapping
    test_headings = [
        "I. INTRODUCTION",
        "A. Background", 
        "1. The Facts",
        "i. Details",
        "Regular paragraph"
    ]
    
    mapped = map_headings(test_headings)
    expected_headings = [
        "# I. INTRODUCTION",
        "## A. Background",
        "### 1. The Facts", 
        "#### i. Details",
        "Regular paragraph"
    ]
    
    if mapped == expected_headings:
        print("✅ Heading mapping works correctly")
    else:
        print(f"❌ Heading mapping failed. Got: {mapped}")
    
    # Test paragraph joining
    test_para_lines = [
        "This is the first sentence. This is the second",
        "sentence that continues from the previous line.",
        "",
        "This is a new paragraph that follows standard",
        "paragraph rules with proper spacing."
    ]
    
    joined = join_lines_to_paragraphs(test_para_lines)
    if len(joined) == 2 and "first sentence. This is the second sentence that continues" in joined[0]:
        print("✅ Paragraph joining works correctly")
    else:
        print(f"❌ Paragraph joining failed. Got: {joined}")

def test_with_sample_pdf(pdf_path: Path):
    """Test conversion with an actual PDF file."""
    print(f"\n📄 Testing with PDF: {pdf_path}")
    
    if not pdf_path.exists():
        print(f"❌ PDF file not found: {pdf_path}")
        return False
    
    # Test PDF text extraction
    try:
        pages = extract_pdf_text_with_blocks(pdf_path)
        print(f"✅ Successfully extracted {len(pages)} pages from PDF")
        
        # Show sample of extracted text
        if pages:
            sample = pages[0][:200] + "..." if len(pages[0]) > 200 else pages[0]
            print(f"📋 First page sample: {repr(sample)}")
    except Exception as e:
        print(f"❌ PDF text extraction failed: {e}")
        return False
    
    # Test full conversion
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            
            success, md_path, meta_path = convert_pdf_to_markdown(
                pdf_path=pdf_path,
                output_dir=output_dir,
                inline_footnotes=False
            )
            
            if success and md_path:
                print("✅ PDF conversion successful")
                
                # Check markdown content
                md_content = md_path.read_text(encoding='utf-8')
                print(f"📊 Conversion stats:")
                print(f"   - Markdown length: {len(md_content)} characters")
                print(f"   - Paragraphs: {md_content.count(chr(10) + chr(10))}")
                print(f"   - Headings: {md_content.count('#')}")
                
                # Show sample of markdown
                sample = md_content[:300] + "..." if len(md_content) > 300 else md_content
                print(f"📝 Markdown sample:\n{sample}")
                
                # Check metadata
                if meta_path:
                    meta_content = json.loads(meta_path.read_text(encoding='utf-8'))
                    print(f"📋 Extracted metadata:")
                    for key, value in meta_content.items():
                        if value:
                            print(f"   - {key}: {value}")
                
                return True
            else:
                print("❌ PDF conversion failed")
                return False
                
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return False

def main():
    """Main test function."""
    print("🚀 Testing Michigan Court PDF to Markdown Converter")
    print("=" * 50)
    
    # Test basic functionality first
    test_basic_functionality()
    
    # Look for sample PDF files to test with
    current_dir = Path(__file__).parent
    sample_pdfs = list(current_dir.glob("*.pdf"))
    
    if sample_pdfs:
        print(f"\n📁 Found {len(sample_pdfs)} PDF file(s) for testing:")
        for pdf in sample_pdfs:
            print(f"   - {pdf.name}")
        
        # Test with the first PDF found
        test_with_sample_pdf(sample_pdfs[0])
    else:
        print("\n📁 No sample PDF files found in current directory")
        print("💡 To test with a real PDF:")
        print(f"   1. Place a Michigan court PDF in: {current_dir}")
        print(f"   2. Run: python {Path(__file__).name}")
        print("   3. Or run: python pdf2md_core.py <pdf_file> <output_dir>")
    
    print("\n" + "=" * 50)
    print("🏁 Testing complete!")
    
    # Show usage examples
    print("\n💡 Usage Examples:")
    print("   # Convert single PDF")
    print("   python pdf2md_core.py opinion.pdf output/")
    print("")
    print("   # Convert in Python code")
    print("   from pdf2md_core import convert_pdf_to_markdown")
    print("   success, md_path, meta_path = convert_pdf_to_markdown(pdf_path, output_dir)")

if __name__ == "__main__":
    main()