"""
this module transforms and cleans the extracted data
"""

import pandas as pd
import logging

def clean_data(df):
    """
    Cleans the raw DataFrame by handling missing values, renaming columns, etc.

    args:
        df (DataFrame): raw data.

    returns:
        DataFrame: cleaned and transformed data.
    """
    logger = logging.getLogger("pipeline_logger")
    try:
        if df is None:
            logger.warning("Received None dataframe for cleaning")
            return None

        # Example cleaning steps — replace with real transformations
        df = df.dropna(how="all")  # drop rows where all values are NaN
        df = df.fillna(0)  # fill remaining NaNs with 0
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]  # clean column names

        logger.info(f"Data cleaned, new shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error during data cleaning: {e}")
        return None

