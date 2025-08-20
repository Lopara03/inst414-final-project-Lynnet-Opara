"""
This module creates visualizations for data analysis and model results
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging
import pandas as pd

def plot_distribution(df, column, save_path="data/visualizations/"):
    """Plots a histogram for numeric columns."""
    logger = logging.getLogger("pipeline_logger")
    
    try:
        if df is None or column not in df.columns:
            logger.warning(f"Cannot plot: dataframe is None or column '{column}' not found")
            return

        os.makedirs(save_path, exist_ok=True)
        plt.figure(figsize=(8, 6))
        sns.histplot(df[column].dropna(), kde=True, bins=30, color="skyblue")
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")

        file_path = os.path.join(save_path, f"{column}_distribution.png")
        plt.savefig(file_path)
        plt.close()
        logger.info(f"Plot saved to {file_path}")

    except Exception as e:
        logger.error(f"Error plotting column '{column}': {e}")


def plot_correlation_matrix(df, save_path="data/visualizations/"):
    """Plots a correlation heatmap for numeric columns."""
    logger = logging.getLogger("pipeline_logger")

    try:
        if df is None or df.empty:
            logger.warning("Cannot plot correlation matrix: dataframe is None or empty")
            return

        os.makedirs(save_path, exist_ok=True)
        numeric_df = df.select_dtypes(include='number')  # only numeric
        if numeric_df.empty:
            logger.warning("No numeric columns to correlate")
            return

        plt.figure(figsize=(10, 8))
        corr = numeric_df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")

        file_path = os.path.join(save_path, "correlation_heatmap.png")
        plt.savefig(file_path)
        plt.close()
        logger.info(f"Correlation heatmap saved to {file_path}")

    except Exception as e:
        logger.error(f"Error plotting correlation heatmap: {e}")


def plot_bar_counts(df, column, save_path="data/visualizations/"):
    """Plots counts for categorical columns (like Strata)."""
    logger = logging.getLogger("pipeline_logger")

    try:
        if df is None or column not in df.columns:
            logger.warning(f"Cannot plot bar counts: column '{column}' not found")
            return

        os.makedirs(save_path, exist_ok=True)
        plt.figure(figsize=(8, 6))
        sns.countplot(y=df[column], palette="Set2", order=df[column].value_counts().index)
        plt.title(f"Counts of {column}")
        plt.xlabel("Count")
        plt.ylabel(column)

        file_path = os.path.join(save_path, f"{column}_counts.png")
        plt.savefig(file_path)
        plt.close()
        logger.info(f"Bar plot saved to {file_path}")

    except Exception as e:
        logger.error(f"Error plotting bar counts for column '{column}': {e}")
