#Importing Streamlit library for working with it
import streamlit as st

#This is a test function to understand what could happen when I click in the button:
def verify_login(username: str, password: str):
    if username and password:
        st.success("Credentials received successfully!", width="stretch")
    
    else:
        st.warning("Empty credentials not allowed! Try again", width="stretch")

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
        verify_login(username, password)