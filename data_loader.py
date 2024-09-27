import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection

# Create a connection object.
conn = st.connection("s3", type=FilesConnection)


# Cache the data loading function
@st.cache_data
def load_data():
    df = conn.read(
        "dulles-weather--use1-az4--x-s3/kiad.csv", input_format="csv", ttl=600
    )
    df["datetime"] = pd.to_datetime(df["datetime"], format="%m/%d/%y %H:%M")
    df["datetime"] = df["datetime"].dt.strftime("%Y-%m-%d")
    df["total_event_sn"] = df["total_event_sn"].fillna("-")
    return df
