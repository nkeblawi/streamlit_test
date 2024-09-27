import pandas as pd
import streamlit as st


# Cache the data loading function
@st.cache_data
def load_data():
    df = pd.read_csv("data/kiad.csv")
    df["datetime"] = pd.to_datetime(df["datetime"], format="%m/%d/%y %H:%M")
    df["datetime"] = df["datetime"].dt.strftime("%Y-%m-%d")
    df["total_event_sn"] = df["total_event_sn"].fillna("-")
    return df
