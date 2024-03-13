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

# Define stages and their corresponding time records
stages = ["Cryptography", "Flowcharts", "Pseudocode"]
time_records = {stage: 0 for stage in stages}

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

# Initialize session state
session_state = st.session_state
if "current_stage_index" not in session_state:
    session_state.current_stage_index = 0

def main():
    st.title("Tech Quest")
    st.sidebar.title("Navigation")
    page_index = st.sidebar.radio("Go to", stages, index=session_state.current_stage_index)
    session_state.current_stage_index = page_index

    current_stage = stages[session_state.current_stage_index]

    if current_stage == "Cryptography":
        display_cryptography()
    elif current_stage == "Flowcharts":
        display_flowcharts()
    elif current_stage == "Pseudocode":
        display_pseudocode()

def display_cryptography():
    st.header("Stage 1: Cryptography")
    password = st.text_input("Enter the password to proceed:")
    if password == stage_passwords["Cryptography"]:
        st.write("Password accepted! You can now proceed to the next stage.")
        if st.button("Next"):
            session_state.current_stage_index += 1
    else:
        st.write("Please enter the correct password to proceed.")

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
