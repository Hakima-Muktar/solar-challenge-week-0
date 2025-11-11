import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, plot_boxplot

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("☀️ Solar Irradiance Dashboard")
st.write("Visualize GHI, DNI, and DHI data interactively for each country.")
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox(
    "Select Country",
    options=["Benin", "Sierra Leone", "Togo"]
)
df = load_data(selected_country)

if df is not None:
    st.subheader(f"Data Overview: {selected_country}")
    st.dataframe(df.head())
    st.subheader("GHI Distribution")
    fig = plot_boxplot(df, selected_country)
    st.pyplot(fig)
    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

else:
    st.warning("No data available for the selected country. Please check your CSV path.")
