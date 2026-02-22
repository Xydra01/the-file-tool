from PIL import Image
import vl_convert as vlc
import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def convert_image(input_path, output_path, input_ext, output_format):
    
    
    if input_ext == 'svg':
        
        with open(input_path, 'r') as f:
            svg_data = f.read()
            
        if output_format in ['jpg', 'jpeg']:
            image_bytes = vlc.svg_to_jpeg(svg_data)
            with open(output_path, 'wb') as f:
                f.write(image_bytes)
            logger.info('Conversion successful: SVG to JPEG')
            
        elif output_format == 'png':
            image_bytes = vlc.svg_to_png(svg_data)
            with open(output_path, 'wb') as f:
                f.write(image_bytes)
            logger.info('Conversion successful: SVG to PNG')
        else:
            raise ValueError(f"Conversion from SVG to {output_format} is not supported.")
        
        return output_path

    
    if output_format == 'svg':
        raise ValueError('Conversion into SVG is not currently supported.')

    
    image = Image.open(input_path)

    if input_ext == 'png' and output_format in ['jpg', 'jpeg']:
        
        image = image.convert('RGB')
        image.save(output_path)
        logger.info('Conversion successful: PNG to JPEG')

    elif input_ext in ['jpg', 'jpeg'] and output_format == 'png':
        image.save(output_path)
        logger.info('Conversion successful: JPEG to PNG')
        
    else:
        raise ValueError(f"Conversion from {input_ext} to {output_format} not mapped.")

    return output_path