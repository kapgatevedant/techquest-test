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
    
    for i, stage in enumerate(stages, start=1):
        st.header(f"Stage {i}: {stage}")
        with st.expander(f"Click here to start Stage {i}"):
            # Display stage content (e.g., cards with questions)
            display_stage_content(stage)
            # Record time taken for the stage
            time_taken = record_time(stage)
            time_records[stage] = time_taken

    # Display final results
    st.header("Final Results")
    display_results()

def display_stage_content(stage):
    # Display stage content (e.g., questions on cards)
    st.write(f"This is where you'd display the content for {stage} stage.")

def record_time(stage):
    # Record time taken for the stage
    start_time = datetime.now()
    st.write("Timer started...")
    # Assuming participants interact with the stage content
    st.write("Participant interacted with stage content...")
    end_time = datetime.now()
    time_taken = (end_time - start_time).total_seconds()
    st.write(f"Time taken for {stage}: {time_taken} seconds")
    return time_taken

def display_results():
    # Display final results with time taken for each stage
    for stage, time_taken in time_records.items():
        st.write(f"Time taken for {stage}: {time_taken} seconds")

if __name__ == "__main__":
    main()
