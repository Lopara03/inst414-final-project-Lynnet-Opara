"""
this module transforms and cleans the extracted data
"""

import pandas as pd
import logging

def clean_data(df):
    """
    Cleans the raw DataFrame by handling missing values, renaming columns, 
    and converting numeric columns for adult depression dataset.

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

        # drop rows where all values are NaN
        df = df.dropna(how="all")

        # normalize column names
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        # convert numeric columns
        numeric_cols = ['frequency', 'weighted_frequency', 'percent', 
                        'lower_95%_cl', 'upper_95%_cl']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        logger.info(f"Data cleaned, new shape: {df.shape}")
        return df

    except Exception as e:
        logger.error(f"Error during data cleaning: {e}")
        return None
