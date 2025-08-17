"""
this file extracts data from external sources (Healthy Minds, YRBSS)
"""

import pandas as pd
import logging

def extract_hms(filepath):
    """Loads HMS survey CSV into a DataFrame."""
    logger = logging.getLogger("pipeline_logger")
    try:
        df = pd.read_csv(filepath)
        logger.info(f"HMS data loaded from {filepath}, shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error loading HMS data: {e}")
        return None

def extract_yrbss(filepath):
    """Loads YRBSS CSV into a DataFrame."""
    logger = logging.getLogger("pipeline_logger")
    try:
        df = pd.read_csv(filepath)
        logger.info(f"YRBSS data loaded from {filepath}, shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error loading YRBSS data: {e}")
        return None
