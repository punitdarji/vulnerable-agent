import streamlit as st
import base64
import yaml
import os

def display_instructions():
    # Markdown with some basic CSS styles for the box
    box_css = """
    <style>
        .instructions-box {
            background-color: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
        }
    </style>
    """

    st.sidebar.markdown(box_css, unsafe_allow_html=True)

    st.sidebar.markdown(
        """
    <div class="instructions-box">
        
    ### Instructions
    This is Demo Application to Undersstand the LLM Agent Attacks:

    Punit Darji has created this application with reference to Pentesting Exam
    </div>

    """,
        unsafe_allow_html=True,
    )

    if st.sidebar.button('Use database schema', use_container_width=True):
        st.sidebar.info('Users(userId,username,password)\n\nTransactions(transactionId,username,reference,recipient,amount)')



# Function to convert image to base64
def get_image_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

def display_logo():
    # Convert your image
    image_base64 = get_image_base64("labs.png")

    # URL of the company website
    url = 'https://www.youtube.com/punitdarji1871'

    # HTML for centered image with hyperlink
    html_string = f"""
    <div style="display:flex; justify-content:center;">
        <a href="{url}" target="_blank">
         <img src="data:image/png;base64,{image_base64}" width="150px">
        </a>
    </div>
    """
    # Display the HTML in the sidebar
    st.sidebar.markdown(html_string, unsafe_allow_html=True)

def _load_llm_config():
    with open('llm-config.yaml', 'r') as f:
        yaml_data = yaml.load(f, Loader=yaml.SafeLoader)
    return yaml_data

def fetch_model_config():
    chosen_model_name = os.getenv("model_name")
    llm_config = _load_llm_config()
    for model_config in llm_config.get("models"):
        if chosen_model_name == model_config.get("model_name"):
            return model_config.get("model")
    else:
        return llm_config.get("default_model")