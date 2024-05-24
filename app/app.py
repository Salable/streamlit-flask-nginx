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
key=st.text_input("Enter the key", "name")
value=st.text_area("Enter the value", "John Doe")
if st.button("Call the API"):
    st.write(f'/api/{path}')
    st.write(f'key: {key}')
    st.write(f'value: {value}')
    st.write(call_flask_api(path, key, value))

st.header("Embedding a Processing Sketch in Streamlit")
st.write("This accesses the API as well, using loadJSON(), and renders it in a full screen canvas.")
url=st.text_input("Enter the URL to embed", "/web/index.html")
# embed streamlit docs in a streamlit app
components.iframe(src=url, height=500, width=700, scrolling=False)
st.markdown("[Open in Browser](/web/index.html)")