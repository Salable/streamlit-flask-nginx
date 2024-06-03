import streamlit as st
import requests 
import streamlit.components.v1 as components
import miro_api
import extra_streamlit_components as stx
import datetime
import string
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from helper import extract_visible_text, remove_punctuation_and_lowercase
import time
from salable import SalableClient, SalableSDKError, PaymentLinkError, PlanError, ProductError, LicenseError, PaymentLinkError
import os

load_dotenv()
client = SalableClient()


@st.cache_resource( experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()
cookie_manager = get_manager()

miro = miro_api.Miro()
api = None

def build_sidebar(auth, board, api):
    with st.sidebar:
        if auth:
            st.write(f"Logged in")
            st.write("Board: ", board)
            if board != None:
                st.write(f"Board: {api.get_specific_board(board_id=board)["name"]}")
                st.html(f"""<a href='https://miro.com/app/board/{board}' target='_blank'>View Board</a>""")

        else: 
            st.html(f"""<a href="{miro.auth_url}" target="_self">Sign in with Miro</a>""")

if "board" in st.query_params:
    st.session_state["board"]=st.query_params["board"]

if "code" in st.query_params:
    code=st.query_params["code"]
    st.query_params.clear()
    auth_token=miro.exchange_code_for_access_token(code) 
    cookie_manager.set("auth", auth_token)

st.session_state["auth_code"]=cookie_manager.get(cookie="auth")
if st.session_state["auth_code"]:
    st.write("Found auth code")
    api = miro_api.MiroApi(st.session_state["auth_code"])
else:
    st.write("can't find it")
            
if "board" not in st.session_state and st.session_state["auth_code"]:
    st.write("# Choose a Board")
    query=st.text_input("Search for Board")
    if query:
        boards = api.get_boards(query=query)
        for board in boards.data:        
            st.html(f"""<a href='/?board={board.id}' target='_self'>{board.name}</a>""") 
if "board" in st.session_state and st.session_state["auth_code"]:    
    board=api.get_specific_board(board_id=st.session_state["board"])
    st.write(f"""# {board.name}""")
    components.iframe(board.view_link, width=700, height=500)    
    st.markdown("### Board Text")
    words={}
    for item in api.get_items(board_id=st.session_state["board"], limit="50").data:
        if item.data and item.data.actual_instance:
            if item.data.actual_instance:
                if hasattr(item.data.actual_instance, "content"):
                    st.html(item.data.actual_instance.content)
                    visible_text = extract_visible_text(item.data.actual_instance.content)
                    card_words=visible_text.split()
                    for word in card_words:
                        no_punc=remove_punctuation_and_lowercase(word)
                        if word in words:                                                        
                            words[no_punc]=words[no_punc]+1
                        else:
                            words[no_punc]=1                    
            else:
                st.write(item)    
    st.markdown("### Words in Board")
    st.write(words)
elif st.session_state["auth_code"]==None:
    st.html(f"""<a href="{miro.auth_url}" target="_self">Sign in with Miro</a>""")    

build_sidebar(auth=st.session_state["auth_code"], board=st.session_state["board"] if "board" in st.session_state else None, api=api)

if st.button("Buy Now"):
    # Generate a payment link
    try:
        payment_link = client.generate_payment_link(
            plan_id=os.environ["SALABLE_PLAN_ID"],
            purchaser="me",
            grantee="you",
            success_url="https://www.example.com",
            cancel_url="https://www.example.com")
        st.link_button("Buy now", payment_link["checkoutUrl"])
    except PaymentLinkError as e:
        st.write(e)

#     with st.form(key="create_card", clear_on_submit=True):
            
#         card_text=st.text_input("Add a card", key="card_text")


#         # Define the card details
#         card_data = {
#             "data" : {
#                 "content" : card_text
#             }
#         }
#         if st.form_submit_button("Create"):
#         # Create the card on the specified board
#             response = api.create_sticky_note_item(board_id=st.session_state["board"], sticky_note_create_request=card_data)            


# base_url="http://localhost:8080"

# def call_flask_api(path, key, value):
#     response = requests.post(f"{base_url}/api/{path}", json={
#         "key": key,
#         "value" : value
#     })
#     if response.status_code == 200:
#         data = response.json()
#         if data:
#             return data
#     return "Failed to get time"

# # Streamlit app
# st.title("Make a Flask API Call from Streamlit")

# path=st.text_input("Enter the path to the API", "echo")
# key=st.text_input("Enter the key", "hello")
# value=st.text_area("Enter the value", "World")
# if st.button("Make the call!"):
#     st.write(f'/api/{path}')
#     st.write(f'key: {key}')
#     st.write(f'value: {value}')
#     st.write(call_flask_api(path, key, value))


# # embed streamlit docs in a streamlit app
# components.iframe("/web/index.html", height=500)
# st.markdown("[Open in Browser](/web/index.html)")
