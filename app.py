import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from data_loader import load_data  # Import the load_data function

# Title and description
st.title("Display Weather Data for Dulles Airport")
st.write("Enter a date to get historical weather information for that day:")

# Date input
date = st.date_input("Choose the date", value=None)
st.write("Date ranges between January 1, 1962 and October 15, 2024.")

# Load the data (this will use the cached data from data_loader.py)
df = load_data()

# Data transformations
df["datetime"] = pd.to_datetime(df["datetime"])
df["total_event_sn"] = df["total_event_sn"].fillna("-")

# Query the dataset to find the row
selected_row = df[df["datetime"] == str(date)]


if st.button("Get Data"):
    # Error checking: handle if no data is found
    if selected_row.empty:
        st.error("No data available for this date.")
    else:
        # Display the weather data if available

        # Create two columns with a 1:1 ratio
        col1, col2 = st.columns(2)

        # Column 1 for Temperatures
        with col1:
            st.subheader("Temperatures")
            st.write(
                f"**High & Low Temps:** {selected_row['t_max'].values[0]} / {selected_row['t_min'].values[0]} °F"
            )
            # st.write(f"Low Temperature: {selected_row['t_min'].values[0]} °F")
            st.write(f"**Average Temperature:** {selected_row['t_avg'].values[0]} °F")
            st.write(f"**Temp Departure:** {selected_row['departure'].values[0]} °F")
            st.write(f"**Heating Degree Days:** {selected_row['hdd'].values[0]}")
            st.write(f"**Cooling Degree Days:** {selected_row['cdd'].values[0]}")

        # Column 2 for Precipitation
        with col2:
            st.subheader("Precipitation")
            st.write(
                f"**Precipitation:** {selected_row['precipitation'].values[0]} inches"
            )
            st.write(f"**Snowfall:** {selected_row['snowfall'].values[0]} inches")
            st.write(f"**Snow-Water Equivalent:** {selected_row['swe'].values[0]}")
            st.write(
                f"**Total Event Snowfall:** {selected_row['total_event_sn'].values[0]} inches"
            )
            st.write(f"**Snow Depth:** {selected_row['snow_depth'].values[0]} inches")
