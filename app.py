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
    st.subheader("Welcome to the Tech Quest event!")
    st.write("This is an interactive challenge where you'll need to solve tech-themed puzzles to progress through the stages.")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Cryptography", "Flowcharts", "Pseudocode"])
    
    # Display content based on selected page
    if page == "Cryptography":
        display_cryptography()
    elif page == "Flowcharts":
        display_flowcharts()
    elif page == "Pseudocode":
        display_pseudocode()

def display_cryptography():
    st.header("Stage 1: Cryptography")
    with st.expander("Click here to start Cryptography stage"):
        st.write("This is where you'd display the content for the Cryptography stage.")

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
