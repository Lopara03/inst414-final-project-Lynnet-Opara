"""
this module saves the cleaned data to the processed data folder
"""

import logging
import os

def save_data(df, filepath):
    """
    Saves the cleaned DataFrame to a specified location.

    args:
        df (DataFrame): cleaned data.
        filepath (str): destination file path.
    """
    logger = logging.getLogger("pipeline_logger")
    try:
        if df is None:
            logger.warning("No data to save")
            return
        os.makedirs(os.path.dirname(filepath), exist_ok=True)  # create folder if it doesn't exist
        df.to_csv(filepath, index=False)
        logger.info(f"Data saved to {filepath}")
    except Exception as e:
        logger.error(f"Error saving data to {filepath}: {e}")
