import pandas as pd
import polars as pl
import logging

# logging setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def convert_data(input_path, output_path, input_ext, output_format):
    logger.info(f"Processing Data: {input_ext} -> {output_format}")
    
    # 1. CSV to Parquet
    if input_ext == 'csv' and output_format == 'parquet':
        df = pl.read_csv(input_path)
        df.write_parquet(output_path)
        logger.info("Conversion successful: CSV to Parquet")
        
    # 2. Parquet to CSV
    elif input_ext == 'parquet' and output_format == 'csv':
        df = pl.read_parquet(input_path)
        df.write_csv(output_path)
        logger.info("Conversion successful: Parquet to CSV")
        
    # 3. CSV to Excel
    elif input_ext == 'csv' and output_format == 'xlsx':
        df = pd.read_csv(input_path)
        df.to_excel(output_path, index=False)
        logger.info("Conversion successful: CSV to Excel")
        
    # 4. CSV to JSON
    elif input_ext == 'csv' and output_format == 'json':
        df = pd.read_csv(input_path)
        df.to_json(output_path, orient="records")
        logger.info("Conversion successful: CSV to JSON")

    else:
        raise ValueError(f"Data conversion from {input_ext} to {output_format} is not supported yet.")

    return output_path