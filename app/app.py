import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("/miro/index.html", height=500)
st.markdown("[Miro](/miro/index.html)")

if st.button("Press"):
    st.write("Pressed!")

