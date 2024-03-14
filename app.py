def main():
    st.title("Tech Quest")
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", stages, index=0)

    if page == "Cryptography":
        if display_cryptography():
            display_flowcharts()
    elif page == "Flowcharts":
        if display_flowcharts():
            display_pseudocode()
    elif page == "Pseudocode":
        display_pseudocode()

def display_cryptography():
    st.header("Stage 1: Cryptography")
    st.subheader("Problem:")
    if st.button("Show Problem"):
        st.write("Here's the problem for the Cryptography stage.")
    st.write("")  # Adding an empty space for better separation
    with st.expander("Click here to start Cryptography stage"):
        st.write("This is where you'd display the content for the Cryptography stage.")
    st.subheader("Enter the password to proceed:")
    password = st.text_input("Password")
    if password == stage_passwords["Cryptography"]:
        if st.button("Next"):
            return True
    else:
        st.write("Please enter the correct password to proceed.")
    return False

def display_flowcharts():
    st.header("Stage 2: Flowcharts")
    st.subheader("Problem:")
    if st.button("Show Problem"):
        st.write("Here's the problem for the Flowcharts stage.")
    st.write("")  # Adding an empty space for better separation
    with st.expander("Click here to start Flowcharts stage"):
        st.write("This is where you'd display the content for the Flowcharts stage.")
    st.subheader("Enter the password to proceed:")
    password = st.text_input("Password")
    if password == stage_passwords["Flowcharts"]:
        if st.button("Next"):
            return True
    else:
        st.write("Please enter the correct password to proceed.")
    return False

def display_pseudocode():
    st.header("Stage 3: Pseudocode")
    st.subheader("Problem:")
    if st.button("Show Problem"):
        st.write("Here's the problem for the Pseudocode stage.")
    st.write("")  # Adding an empty space for better separation
    with st.expander("Click here to start Pseudocode stage"):
        st.write("This is where you'd display the content for the Pseudocode stage.")
    st.subheader("Enter the password to proceed:")
    password = st.text_input("Password")
    if password == stage_passwords["Pseudocode"]:
        if st.button("Next"):
            return True
    else:
        st.write("Please enter the correct password to proceed.")
    return False
