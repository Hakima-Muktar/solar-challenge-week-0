import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, plot_boxplot
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("Solar Irradiance Dashboard")
st.write("Visualize GHI, DNI, and DHI data interactively for each country.")
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox(
    "Select Country",
    options=["All", "Benin", "Sierra Leone", "Togo"]
)
df_all = load_data("All")
if selected_country != "All":
    df = load_data(selected_country)
else:
    df = df_all

st.subheader(f"Data Overview: {selected_country}")
st.dataframe(df.head())

if selected_country == "All":
    st.subheader("Metric Comparison Across Countries")
    metrics = ['GHI', 'DNI', 'DHI']
    for metric in metrics:
        if metric in df.columns:
            fig, ax = plt.subplots(figsize=(8,4))
            sns.boxplot(x='Country', y=metric, data=df, ax=ax)
            ax.set_title(f"{metric} Comparison Across Countries")
            st.pyplot(fig)

    cols_to_summarize = [c for c in metrics if c in df.columns]
    if cols_to_summarize:
        summary = df.groupby('Country')[cols_to_summarize].agg(['mean','median','std'])
        st.subheader("Summary Statistics by Country")
        st.dataframe(summary)
else:
    st.subheader(f"{selected_country} - GHI Distribution")
    if 'GHI' in df.columns:
        fig = plot_boxplot(df, selected_country)
        st.pyplot(fig)
    st.subheader(f"{selected_country} - Summary Statistics")
    st.dataframe(df.describe())
