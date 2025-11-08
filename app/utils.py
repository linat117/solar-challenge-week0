# app/utils.py

import pandas as pd
import numpy as np
import os

# Function to load data
def load_data(country_name: str):
    """
    Load cleaned dataset based on the selected country.
    """
    file_path = f"data/{country_name}_clean.csv"  # assumes your CSVs are in /data
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    return pd.read_csv(file_path)

# Function to get summary KPIs
def get_summary_stats(df):
    """
    Return key metrics from dataset.
    """
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Mean GHI": df["GHI"].mean(),
        "Mean DNI": df["DNI"].mean(),
        "Mean WS": df["WS"].mean(),
    }
