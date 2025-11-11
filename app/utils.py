
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
FILES = {
    "Benin": "data/benin-malanville.csv",
    "Sierra Leone": "data/sierraleone-bumbuna.csv",
    "Togo": "data/togo-dapaong_qc.csv"
}

def load_data(country):
    """Load CSV for a single country or all countries."""
    dfs = []
    if country == "All":
        for c, path in FILES.items():
            if os.path.exists(path):
                df = pd.read_csv(path)
                df["Country"] = c
                dfs.append(df)
            else:
                print(f" File not found for {c}: {path}")
        if dfs:
            return pd.concat(dfs, ignore_index=True)
        else:
            return pd.DataFrame() 
    else:
        path = FILES.get(country)
        if path and os.path.exists(path):
            df = pd.read_csv(path)
            df["Country"] = country
            return df
        else:
            print(f"File not found for {country}: {path}")
            return pd.DataFrame()

def plot_boxplot(df, country, column="GHI"):
    """Plot a boxplot for the given column."""
    if column not in df.columns:
        print(f"⚠️ Column '{column}' not found in data")
        return plt.figure()
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(y=df[column], ax=ax)
    ax.set_title(f"{column} Distribution - {country}")
    return fig
