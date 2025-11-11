import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_data(country: str):
    """Load CSV data based on country name."""
    data_files = {
        "Benin": "data/benin-malanville.csv",
        "Sierra Leone": "data/sierraleone-bumbuna.csv",
        "Togo": "data/togo-dapaong_qc.csv",
    }

    file_path = data_files.get(country)
    if not file_path or not os.path.exists(file_path):
        print(f" File not found for {country}: {file_path}")
        return None
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading {country} data: {e}")
        return None
def plot_boxplot(df: pd.DataFrame, country: str):
    """Create a boxplot for GHI values."""
    if 'GHI' not in df.columns:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, 'No GHI column found', ha='center', va='center')
        ax.axis('off')
        return fig

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(y=df['GHI'], ax=ax)
    ax.set_title(f"GHI Distribution - {country}")
    ax.set_ylabel("GHI")
    return fig
