#Importing Streamlit library for working with it
import streamlit as st
#Temporal modification for accessing to the data
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

#Importing the authentication flow already done previously (can you see how beautiful is the responsibilities separation baby?)
from auth import verify_credentials

#Modifying the Browser tab: If you want to change the emoji, access to the emoji shortcodes:
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(page_title="TaskManager - Login", page_icon=":rocket:")
# Declare alias for st.session_state, just for convenience. The session state is important because
#Keeps the information available between reruns, and I can access to the element in an easier way.
#Use callbacks to update state when interacting with widgets.
#NOTE: The state here is temporal. Later, we will move to the app.py file
state = st.session_state

#We will initialize the authenticated state, and we will avoid to keep a past state in the future.
if "authenticated" not in state:
    state.authenticated = False

#Encapsulating the login in a function for using in app.py
def show_login():
    #First title of our page
    st.title("Welcome to Task Manager!")
    st.header("Before to start, let's check your identity")

    #Creating the login form. We will watch constantly the expression "with". This is a command that can allow us to manage the resources or
    #structures in a safer way, capturing and handling errors efficiently.
    # In this application, defines the context in which the form's widgets are created.
    # It groups the input fields and the submit button into a single form.
    with st.form(key="my_form"):
        username = st.text_input(label="Enter your Username", placeholder="Your username here")
        password = st.text_input(label="Enter your password", type="password",  # Masks the input 
        placeholder="Your secret password")
        #When I click in the button, the system will execute the function passing the user and the password for validation
        if st.form_submit_button("Login"):
            #We will verify that we don't have empty credentials, but in a more direct way:
            if not username or not password:
                st.warning("Empty credentials not allowed! Try again")

            #Time to verify the credentials using the function declared in auth:
            elif verify_credentials(username, password):
                #Store the value in the session state if the login process is true
                state.authenticated = True
                st.success("Welcome to Task Manager! Redirecting to your dashboard...")

            else:
                #Store the value in the session state if the login process is false
                state.authenticated = False
                st.error("Invalid credentials! Verify your information and try again")