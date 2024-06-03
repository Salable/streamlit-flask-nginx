import streamlit as st
import requests 
import streamlit.components.v1 as components
import miro_api
import extra_streamlit_components as stx
import datetime
import string
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def extract_visible_text(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract and return visible text
    visible_text = soup.get_text()
    return visible_text

def remove_punctuation_and_lowercase(input_string):
    # Remove punctuation
    no_punctuation = input_string.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    result = no_punctuation.lower()
    return result

def debug():
    st.write("## Debug")
    st.write(st.session_state)
    st.write(st.query_params)
    st.write(api)
    st.write(auth_code)