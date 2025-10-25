#!/usr/bin/env python3
"""
Example implementations showing how to integrate the Michigan Court
PDF to Markdown converter into different types of systems.
"""

from pathlib import Path
from pdf2md_core import convert_pdf_to_markdown
import json
import tempfile
import sys

# ========================================
# Example 1: Simple Batch Processor
# ========================================

def batch_convert_directory(input_dir: str, output_dir: str):
    """
    Convert all PDFs in a directory to Markdown files.
    
    Args:
        input_dir: Path to directory containing PDF files
        output_dir: Path to directory for output files
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists():
        print(f"❌ Input directory not found: {input_dir}")
        return
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all PDF files
    pdf_files = list(input_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return
    
    print(f"🔄 Converting {len(pdf_files)} PDF files...")
    
    successful = 0
    failed = 0
    
    for pdf_file in pdf_files:
        print(f"Processing {pdf_file.name}...", end=" ")
        
        success, md_path, meta_path = convert_pdf_to_markdown(
            pdf_path=pdf_file,
            output_dir=output_path,
            inline_footnotes=False
        )
        
        if success:
            print("✅")
            successful += 1
        else:
            print("❌")
            failed += 1
    
    print(f"\n📊 Results: {successful} successful, {failed} failed")

# ========================================
# Example 2: Web API Server
# ========================================

def create_web_api():
    """
    Example Flask web API for PDF conversion.
    
    Endpoints:
        POST /convert - Upload PDF and get Markdown
        GET /health - Health check
    """
    try:
        from flask import Flask, request, jsonify, make_response
    except ImportError:
        print("Flask not installed. Run: pip install flask")
        return
    
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    
    @app.route('/health', methods=['GET'])
    def health_check():
        """Health check endpoint."""
        return jsonify({'status': 'healthy', 'service': 'pdf-to-markdown'})
    
    @app.route('/convert', methods=['POST'])
    def convert_pdf_endpoint():
        """Convert uploaded PDF to Markdown."""
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'File must be a PDF'}), 400
        
        # Process the file
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir = Path(temp_dir)
                
                # Save uploaded file
                pdf_path = temp_dir / file.filename
                file.save(pdf_path)
                
                # Convert to markdown
                success, md_path, meta_path = convert_pdf_to_markdown(
                    pdf_path=pdf_path,
                    output_dir=temp_dir,
                    inline_footnotes=request.form.get('inline_footnotes', 'false').lower() == 'true'
                )
                
                if success and md_path:
                    # Read results
                    markdown_content = md_path.read_text(encoding='utf-8')
                    
                    metadata = {}
                    if meta_path:
                        metadata = json.loads(meta_path.read_text(encoding='utf-8'))
                    
                    return jsonify({
                        'success': True,
                        'filename': file.filename,
                        'markdown': markdown_content,
                        'metadata': metadata,
                        'stats': {
                            'length': len(markdown_content),
                            'paragraphs': markdown_content.count('\n\n'),
                            'headings': markdown_content.count('#')
                        }
                    })
                else:
                    return jsonify({'error': 'Conversion failed'}), 500
                    
        except Exception as e:
            return jsonify({'error': f'Processing error: {str(e)}'}), 500
    
    return app

# ========================================
# Example 3: Command Line Tool
# ========================================

def create_cli_tool():
    """
    Example command line interface using argparse.
    """
    import argparse
    
    def main():
        parser = argparse.ArgumentParser(
            description='Convert Michigan Court PDFs to Markdown',
            epilog='Example: python examples.py convert input.pdf output/ --inline-footnotes'
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Convert command
        convert_parser = subparsers.add_parser('convert', help='Convert PDF(s) to Markdown')
        convert_parser.add_argument('input', help='PDF file or directory')
        convert_parser.add_argument('output', help='Output directory')
        convert_parser.add_argument('--inline-footnotes', action='store_true',
                                   help='Convert footnote numbers to inline format')
        convert_parser.add_argument('--verbose', '-v', action='store_true',
                                   help='Verbose output')
        
        # Batch command
        batch_parser = subparsers.add_parser('batch', help='Batch convert directory')
        batch_parser.add_argument('input_dir', help='Input directory containing PDFs')
        batch_parser.add_argument('output_dir', help='Output directory for Markdown files')
        
        # Info command
        info_parser = subparsers.add_parser('info', help='Show PDF information')
        info_parser.add_argument('pdf_file', help='PDF file to analyze')
        
        args = parser.parse_args()
        
        if args.command == 'convert':
            input_path = Path(args.input)
            output_path = Path(args.output)
            
            if input_path.is_file():
                # Single file conversion
                success, md_path, meta_path = convert_pdf_to_markdown(
                    input_path, output_path, args.inline_footnotes
                )
                
                if success:
                    print(f"✅ Converted: {md_path}")
                    if args.verbose and meta_path:
                        metadata = json.loads(meta_path.read_text())
                        print("📋 Metadata:")
                        for key, value in metadata.items():
                            if value:
                                print(f"   {key}: {value}")
                else:
                    print("❌ Conversion failed")
                    sys.exit(1)
            
            elif input_path.is_dir():
                # Directory conversion
                batch_convert_directory(str(input_path), str(output_path))
        
        elif args.command == 'batch':
            batch_convert_directory(args.input_dir, args.output_dir)
        
        elif args.command == 'info':
            # Show PDF information
            from pdf2md_core import extract_pdf_text_with_blocks, extract_meta_from_pages
            
            pdf_path = Path(args.pdf_file)
            if not pdf_path.exists():
                print(f"❌ PDF file not found: {pdf_path}")
                sys.exit(1)
            
            try:
                pages = extract_pdf_text_with_blocks(pdf_path)
                metadata = extract_meta_from_pages(pages)
                
                print(f"📄 PDF Information: {pdf_path.name}")
                print(f"   Pages: {len(pages)}")
                print(f"   Total characters: {sum(len(p) for p in pages)}")
                print("\n📋 Extracted Metadata:")
                for key, value in metadata.items():
                    if value:
                        print(f"   {key}: {value}")
                
                if pages:
                    sample = pages[0][:200] + "..." if len(pages[0]) > 200 else pages[0]
                    print(f"\n📝 First page sample:\n{sample}")
                    
            except Exception as e:
                print(f"❌ Error analyzing PDF: {e}")
                sys.exit(1)
        
        else:
            parser.print_help()
    
    return main

# ========================================
# Example 4: Database Integration
# ========================================

class DocumentProcessor:
    """
    Example class for processing and storing converted documents.
    """
    
    def __init__(self, database_url=None):
        self.database_url = database_url
        # In a real implementation, you'd initialize your database connection here
    
    def process_pdf(self, pdf_path: Path, store_in_db: bool = True):
        """
        Process a PDF and optionally store results in database.
        
        Args:
            pdf_path: Path to PDF file
            store_in_db: Whether to store results in database
            
        Returns:
            Dictionary with processing results
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = Path(temp_dir)
            
            # Convert PDF
            success, md_path, meta_path = convert_pdf_to_markdown(
                pdf_path=pdf_path,
                output_dir=temp_dir,
                inline_footnotes=True
            )
            
            if not success:
                return {'success': False, 'error': 'Conversion failed'}
            
            # Read results
            markdown_content = md_path.read_text(encoding='utf-8')
            metadata = {}
            if meta_path:
                metadata = json.loads(meta_path.read_text(encoding='utf-8'))
            
            result = {
                'success': True,
                'filename': pdf_path.name,
                'markdown': markdown_content,
                'metadata': metadata,
                'stats': {
                    'length': len(markdown_content),
                    'word_count': len(markdown_content.split()),
                    'paragraph_count': markdown_content.count('\n\n'),
                    'heading_count': markdown_content.count('#')
                }
            }
            
            # Store in database if requested
            if store_in_db:
                self._store_document(result)
            
            return result
    
    def _store_document(self, doc_data):
        """
        Store document data in database.
        This is a placeholder for your database integration.
        """
        print(f"📀 Storing document: {doc_data['filename']}")
        # Your database storage logic here
        pass
    
    def process_directory(self, directory_path: Path):
        """Process all PDFs in a directory."""
        pdf_files = list(directory_path.glob("*.pdf"))
        results = []
        
        for pdf_file in pdf_files:
            print(f"Processing {pdf_file.name}...")
            result = self.process_pdf(pdf_file)
            results.append(result)
        
        return results

# ========================================
# Example Usage
# ========================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("📚 PDF to Markdown Converter - Example Implementations")
        print("\nUsage:")
        print("  python examples.py batch <input_dir> <output_dir>")
        print("  python examples.py server")
        print("  python examples.py cli [args...]")
        print("  python examples.py test")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "batch":
        if len(sys.argv) != 4:
            print("Usage: python examples.py batch <input_dir> <output_dir>")
            sys.exit(1)
        batch_convert_directory(sys.argv[2], sys.argv[3])
    
    elif command == "server":
        app = create_web_api()
        if app:
            print("🚀 Starting web server on http://127.0.0.1:5000")
            print("📝 Upload PDFs to: POST http://127.0.0.1:5000/convert")
            app.run(debug=True, port=5000)
    
    elif command == "cli":
        cli_main = create_cli_tool()
        # Remove the first two arguments (python examples.py cli)
        sys.argv = sys.argv[2:]
        cli_main()
    
    elif command == "test":
        # Test with document processor
        processor = DocumentProcessor()
        print("🧪 Testing document processor...")
        
        # Look for sample PDFs
        current_dir = Path(".")
        sample_pdfs = list(current_dir.glob("*.pdf"))
        
        if sample_pdfs:
            result = processor.process_pdf(sample_pdfs[0], store_in_db=False)
            print(f"📊 Processing result: {result['success']}")
            if result['success']:
                print(f"   Length: {result['stats']['length']} chars")
                print(f"   Words: {result['stats']['word_count']}")
                print(f"   Paragraphs: {result['stats']['paragraph_count']}")
        else:
            print("No PDF files found for testing")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)