"""
this file extracts data from external sources
"""

import pandas as pd
import logging

def extract_adult_depression(filepath):
    """
    Loads the adult depression CSV into a DataFrame.
    
    Args:
        filepath (str): path to adult-depression-lghc-indicator-24.csv
    Returns:
        pd.DataFrame: loaded dataset
    """
    logger = logging.getLogger("pipeline_logger")
    try:
        df = pd.read_csv(filepath, sep=",", engine="python", encoding="utf-8-sig")
        logger.info(f"Adult Depression data loaded from {filepath}, shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error loading Adult Depression data: {e}")
        return None
