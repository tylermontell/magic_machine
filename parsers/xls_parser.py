# parsers/xls_parser.py

import logging
import xml.etree.ElementTree as ET
from config import NAMESPACES

logger = logging.getLogger(__name__)

def parse_xls_file(file_path):
    """
    Parse .xls files (SpreadsheetML XML format).
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []

        # Iterate through the XML structure to extract data
        for row in root.findall('.//ss:Row', namespaces=NAMESPACES):
            row_data = []
            for cell in row.findall('.//ss:Data', namespaces=NAMESPACES):
                row_data.append(cell.text)
            data.append(row_data)
        
        return data

    except Exception as e:
        logger.error(f'Error parsing .xls file {file_path}: {e}')
        return []
