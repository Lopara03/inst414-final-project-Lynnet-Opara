
"""
this file extracts data from external sources (Healthy Minds, YRBSS).
"""
import pandas as pd

def extract_hms(filepath):
    """loads HMS survey CSV into a DataFrame."""
    df = pd.read_csv(filepath)
    return df

def extract_yrbss(filepath):
    """loads YRBSS CSV into a DataFrame."""
    df = pd.read_csv(filepath)
    return df
