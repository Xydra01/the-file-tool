from docling.document_converter import DocumentConverter
from pdf2docx import Converter
from markitdown import MarkItDown
import logging
import json

# logging setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def convert_document(input_path, output_path, input_ext, output_format):
    logger.info(f"Processing Document: {input_ext} -> {output_format}")

    # PDF to Word
    if input_ext == 'pdf' and output_format == 'docx':
        cv = Converter(input_path)
        cv.convert(output_path) # Converts all pages by default
        cv.close()
        logger.info("Conversion successful: PDF to DOCX")

    # PDF/Word/HTML to Markdown
    elif input_ext in ['pdf', 'docx', 'html'] and output_format == 'md':
        md = MarkItDown()
        result = md.convert(input_path)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        logger.info(f"Conversion successful: {input_ext.upper()} to Markdown")

    # PDF/Word/HTML to JSON
    elif input_ext in ['pdf', 'docx', 'html'] and output_format == 'json':
        doc_converter = DocumentConverter()
        result = doc_converter.convert(input_path)
        
        # Export Docling's parsed document structure to a dictionary, then save as JSON
        doc_dict = result.document.export_to_dict()
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(doc_dict, f, indent=2)
        logger.info(f"Conversion successful: {input_ext.upper()} to JSON")

    else:
        raise ValueError(f"Document conversion from {input_ext} to {output_format} is not supported yet.")

    return output_path