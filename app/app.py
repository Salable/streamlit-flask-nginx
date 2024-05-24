import streamlit as st
import requests 
import streamlit.components.v1 as components

base_url="http://localhost:8080"

def call_flask_api(path, key, value):
    response = requests.post(f"{base_url}/api/{path}", json={
        "key": key,
        "value" : value
    })
    if response.status_code == 200:
        data = response.json()
        if data:
            return data
    return "Failed to get time"

# Streamlit app
st.title("Make a Flask API Call from Streamlit")

path=st.text_input("Enter the path to the API", "echo")
key=st.text_input("Enter the key", "hello")
value=st.text_area("Enter the value", "World")
if st.button("Make the call!"):
    st.write(f'/api/{path}')
    st.write(f'key: {key}')
    st.write(f'value: {value}')
    st.write(call_flask_api(path, key, value))


url=st.text_input("Enter the URL to embed", "/web/index.html")
# embed streamlit docs in a streamlit app
components.iframe(url, height=500)
st.markdown("[Open in Browser](/web/index.html)")