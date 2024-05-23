import streamlit as st
import requests
import datetime

base_url="http://localhost:8080"

# Function to get the current time from the Flask API
def get_current_time():
    response = requests.get(f"{base_url}/api/time")
    if response.status_code == 200:
        data = response.json()
        timestamp = data.get("timestamp")
        if timestamp:
            return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return "Failed to get time"

# Streamlit app
st.title("Current Time Fetcher")

if st.button("Get Current Time"):
    current_time = get_current_time()
    st.write(f"Current Time: {current_time}")