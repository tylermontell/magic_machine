# general_parser.py

import os
import logging
from parsers.xls_parser import parse_xls_file
from parsers.xlsx_parser import parse_xlsx_file
from parsers.html_parser import parse_html_file  # Ensure this imports the correct function

logger = logging.getLogger(__name__)

def process_files(trigger_folder):
    """
    Process files in the given trigger folder.
    """
    file_paths = os.listdir(trigger_folder)
    logger.info(f"Found {len(file_paths)} files to process.")

    for file_name in file_paths:
        file_path = os.path.join(trigger_folder, file_name)

        # Skip system files like .DS_Store
        if file_name == '.DS_Store':
            continue
        
        logger.info(f"Processing file: {file_path}")
        try:
            if file_name.endswith('.xls'):
                data = parse_xls_file(file_path)
            elif file_name.endswith('.xlsx'):
                data = parse_xlsx_file(file_path)
            elif file_name.endswith('.html') or file_name.endswith('.htm'):
                # Process HTML files with the updated parse_html_file function
                data = parse_html_file(file_path)
            else:
                logger.warning(f"Unsupported file type: {file_name}")
                continue

            # Process or log the extracted data
            logger.info(f"Processed data: {data}")

        except Exception as e:
            logger.error(f"Error processing file {file_name}: {e}")
