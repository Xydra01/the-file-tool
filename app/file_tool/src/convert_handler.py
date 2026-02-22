import os
import logging

# Import conversion functions
from converters.data_conversion import convert_data
from converters.document_conversion import convert_document
from converters.image_conversion import convert_image

# Logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)



def handle_conversion(input_path: str, output_format: str, output_dir: str = "output"):
    
    # Routing

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Extract the original file extension and clean up the strings
    filename = os.path.basename(input_path)
    name_without_ext, input_ext = os.path.splitext(filename)
    
    input_ext = input_ext.lower().lstrip('.')
    output_format = output_format.lower().lstrip('.')

    # Define where the final converted file will be saved
    output_path = os.path.join(output_dir, f"{name_without_ext}.{output_format}")

    logger.info(f"Routing request: {input_ext} -> {output_format}")

    

    #Image Conversions
    image_formats = {'png', 'jpg', 'jpeg', 'svg'}
    if input_ext in image_formats or output_format in image_formats:
        logger.info("Sending to Image Converter...")
        return convert_image(input_path, output_path, input_ext, output_format)

    #Document Conversions
    document_formats = {'pdf', 'docx', 'doc', 'md', 'html'}
    if input_ext in document_formats or output_format in document_formats:
        logger.info("Sending to Document Converter...")
        return convert_document(input_path, output_path, input_ext, output_format)

    #Data Conversions
    data_formats = {'csv', 'parquet', 'xlsx', 'json', 'arrow'}
    if input_ext in data_formats or output_format in data_formats:
        logger.info("Sending to Data Converter...")
        return convert_data(input_path, output_path, input_ext, output_format)

    # Catch-all for unsupported formats
    raise ValueError(f"Conversion from {input_ext} to {output_format} is not supported in the current scope.")
    

# A quick way to test the handler directly
if __name__ == "__main__":
    pass

