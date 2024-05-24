import streamlit as st
import requests
import datetime

base_url="http://localhost:8080"

def call_flask_api():
    response = requests.post(f"{base_url}/api/store", json={
        "key": "hello",
        "value" : """
        print("World")
        """
    })
    if response.status_code == 200:
        data = response.json()
        if data:
            return data
    return "Failed to get time"

# Streamlit app
st.title("Current Time Fetcher")

if st.button("Get Current Time"):
    st.write(call_flask_api())