import streamlit as st
import openai
import os

from text_summarizer.functions import summarize


# <!> Some testings...
# Automatically reads from the ".streamlit/secrets.toml"... 
# openai.api_key = os.getenv('OPENAI_KEY')  
# print(">> openai.api_key = ", openai.api_key)   # Debug...

##
try:
    # Automatically reads from the ".streamlit/secrets.toml"... 
    openai.api_key = os.getenv('OPENAI_KEY')

    # <!> If changes to ".streamlit/config.toml" are made while the app is running, the server needs 
    #       to be restarted for changes to be reflected in the app.

    ##
    ##
    st.title("Text Summarizer")

    ## Initialize state variable 
    #   The "st.session_state" object is a Python dict that saves data when the app gets rerun. 
    #   The code below is testing to see if there is already an entry for summary. 
    #   If summary is not in "st.session_state", it will get added with its value set to an empty str.
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    input_text = st.text_area(label='Enter full text:', value="", height=250)

    #st.button("submit")
    st.button(
        "Submit",
        on_click=summarize,
        kwargs={"prompt": input_text},
        )

    ## output_text = st.text_area(label='Summarized text:', value='', height=250)
    # configure text area to populate with current state of summary
    output_text = st.text_area(label='Summarized text:', value=st.session_state["summary"], height=250)
except:
    st.write("<!> ERROR: an error occured.")