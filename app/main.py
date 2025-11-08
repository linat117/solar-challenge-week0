# app/main.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_summary_stats

# =============================
# Streamlit Dashboard
# =============================

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("☀️ Solar Data Insights Dashboard")
st.markdown("Visualize and explore solar energy data interactively.")

# Sidebar: Country selector
country = st.sidebar.selectbox(
    "🌍 Select Country",
    ("benin", "sieraleone", "togo")
)

# Load data
try:
    df = load_data(country)
    st.success(f"Loaded data for {country.title()} successfully!")
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

# Display KPIs
st.subheader("📊 Key Performance Indicators")
stats = get_summary_stats(df)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Rows", stats["Rows"])
col2.metric("Columns", stats["Columns"])
col3.metric("Avg GHI", f"{stats['Mean GHI']:.2f}")
col4.metric("Avg WS", f"{stats['Mean WS']:.2f}")

# Select plot type
st.sidebar.markdown("### 📈 Visualization Options")
plot_type = st.sidebar.radio("Select Plot", ("Boxplot", "Scatterplot", "Histogram"))

# Plot
st.subheader(f"🔹 {plot_type} Visualization")

if plot_type == "Boxplot":
    col = st.selectbox("Select column for boxplot:", df.columns)
    fig, ax = plt.subplots()
    sns.boxplot(data=df, y=col, color="skyblue", ax=ax)
    st.pyplot(fig)

elif plot_type == "Scatterplot":
    x_col = st.selectbox("X-axis", df.columns)
    y_col = st.selectbox("Y-axis", df.columns)
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
    st.pyplot(fig)

elif plot_type == "Histogram":
    col = st.selectbox("Select column for histogram:", df.columns)
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax, color="orange")
    st.pyplot(fig)

# Top regions (if available)
if "Region" in df.columns:
    st.subheader("🏆 Top Regions by GHI")
    top_regions = df.groupby("Region")["GHI"].mean().sort_values(ascending=False).head(5)
    st.table(top_regions)
