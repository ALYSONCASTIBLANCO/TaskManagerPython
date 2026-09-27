from CRUD import *
from cli import show_cli
from login import login
import time

def main():
    """Main function of the program."""
    #Rendering the login to validate the credentials:
    successful = login()
    if(successful):
        print("Welcome to the platform user! Redirecting to your CLI...")
        time.sleep(3)
        show_cli()
    else:
        print("Wrong username or password. Try again.")

# This ensures the code runs only when the file is executed directly,
# not when it is imported as a module.
if __name__ == "__main__":
    main()