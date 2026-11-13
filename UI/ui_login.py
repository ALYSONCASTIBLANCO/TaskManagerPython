#Importing Streamlit library for working with it
import streamlit as st

#Importing the authentication flow already done previously (can you see how beautiful is the responsibilities separation baby?)
from auth import verify_credentials

# Declare alias for st.session_state, just for convenience. The session state is important because
#Keeps the information available between reruns, and I can access to the element in an easier way.
#Use callbacks to update state when interacting with widgets.
state = st.session_state

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
                #Once is authenticated, rerun the application to watch the dashboard
                st.rerun()

            else:
                #Store the value in the session state if the login process is false
                state.authenticated = False
                st.error("Invalid credentials! Verify your information and try again")
    