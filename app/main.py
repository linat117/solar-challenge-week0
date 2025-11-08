import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Solar Data Dashboard ☀️",
    page_icon="☀️",
    layout="wide"
)

# ---- APP TITLE ----
st.title("🌍 Solar Data Comparison Dashboard")
st.write("Explore and compare solar energy metrics across countries.")

# ---- SIDEBAR ----
st.sidebar.header("Select Dataset")

# Example countries — update these once you have cleaned CSVs
countries = ["Benin", "Sierra Leone", "Togo"]
selected_country = st.sidebar.selectbox("Choose a country", countries)

# ---- LOAD DATA ----
# Adjust file paths based on your setup
data_path = f"data/{selected_country.lower()}_clean.csv"

@st.cache_data
def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"⚠️ File not found: {path}")
        return None

df = load_data(data_path)

# ---- DISPLAY DATA ----
if df is not None:
    st.subheader(f"📊 {selected_country} Solar Data Overview")
    st.write(df.head())

    # ---- BASIC STATS ----
    st.markdown("### 🌡️ Summary Statistics")
    st.write(df.describe())

    # ---- VISUALIZATION ----
    st.markdown("### ☀️ Solar Irradiance Trends")

    numeric_cols = ["GHI", "DNI", "DHI"]
    selected_metric = st.selectbox("Select a metric to visualize:", numeric_cols)

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(data=df, x=df.index, y=selected_metric, ax=ax)
    ax.set_title(f"{selected_metric} Trend Over Time in {selected_country}")
    ax.set_xlabel("Index (or Time if Timestamp added)")
    ax.set_ylabel(selected_metric)
    st.pyplot(fig)
else:
    st.info("Upload your cleaned dataset to the `data/` folder to get started.")


