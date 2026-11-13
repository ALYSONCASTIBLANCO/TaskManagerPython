import streamlit as st
from UI.ui_login import show_login
from UI.dashboard import show_dashboard
#Modifying the Browser tab: If you want to change the emoji, access to the emoji shortcodes:
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(page_title="TaskManager", page_icon=":rocket:")

# Declare alias for st.session_state, just for convenience. The session state is important because
#Keeps the information available between reruns, and I can access to the element in an easier way.
#Use callbacks to update state when interacting with widgets.
state = st.session_state

#We will initialize the authenticated state, and we will avoid to keep a past state in the future.
if "authenticated" not in state:
    state.authenticated = False

def main():
    """Main function of the program."""
    #This state is now shared. As you remember, authenticated is changing when you inteact with the login, for that reason
    #by default is false, this will allow that the login can be rendered first and then, can start the entire flow. When 
    #becomes True, will render the dashboard.
    if state.authenticated:
        show_dashboard()
    else:
        show_login()

# This ensures the code runs only when the file is executed directly,
# not when it is imported as a module.
if __name__ == "__main__":
    main()