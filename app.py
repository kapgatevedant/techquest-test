# app.py

import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Tech Quest", 
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define stages
stages = ["Cryptography", "Flowcharts", "Pseudocode"]

# Define passwords for each stage
stage_passwords = {
    "Cryptography": "ABCDE",
    "Flowcharts": "FGHIJ",
    "Pseudocode": "KLMNO"
}

# Define dark and purple theme
custom_css = f"""
    <style>
        body {{
            color: #FFFFFF;
            background-color: #23002C;
        }}
        .st-bw {{
            color: #FF00FF;
        }}
        .st-cy {{
            color: #00FFFF;
        }}
        .st-fs {{
            font-size: 20px;
        }}
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

def main():
    st.title("Tech Quest")
    st.sidebar.title("Navigation")
    page_index = st.sidebar.radio("Go to", stages, index=0)

    if page_index == 0:
        display_cryptography()
    elif page_index == 1:
        display_flowcharts()
    elif page_index == 2:
        display_pseudocode()

def display_cryptography():
    st.header("Stage 1: Cryptography")
    password = st.text_input("Enter the password to proceed:")
    if password == stage_passwords["Cryptography"]:
        st.write("Password accepted! You can now proceed to the next stage.")
        if st.button("Next"):
            st.experimental_rerun()

def display_flowcharts():
    st.header("Stage 2: Flowcharts")
    with st.expander("Click here to start Flowcharts stage"):
        st.write("This is where you'd display the content for the Flowcharts stage.")

def display_pseudocode():
    st.header("Stage 3: Pseudocode")
    with st.expander("Click here to start Pseudocode stage"):
        st.write("This is where you'd display the content for the Pseudocode stage.")

if __name__ == "__main__":
    main()
