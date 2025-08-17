"""
this module creates visualizations for data analysis and model results
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging

def plot_distribution(df, column, save_path="data/visualizations/"):
    """
    Plots a histogram for a given column and saves the figure.

    args:
        df (DataFrame): dataset
        column (str): column to plot
        save_path (str): folder path to save plot
    """
    logger = logging.getLogger("pipeline_logger")
    
    try:
        if df is None or column not in df.columns:
            logger.warning(f"Cannot plot: dataframe is None or column '{column}' not found")
            return

        os.makedirs(save_path, exist_ok=True)  # make folder if it doesn't exist

        plt.figure(figsize=(8, 6))
        sns.histplot(df[column], kde=True, bins=30, color="skyblue")
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")

        file_path = os.path.join(save_path, f"{column}_distribution.png")
        plt.savefig(file_path)
        plt.close()
        logger.info(f"Plot saved to {file_path}")

    except Exception as e:
        logger.error(f"Error plotting column '{column}': {e}")
