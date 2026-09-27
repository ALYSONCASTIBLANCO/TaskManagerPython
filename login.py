from auth import *

#Function that contains the login
def login() -> bool:
    print("Welcome to Task Manager!")
    print("Before to start, let's verify who you are!")
    #Asking credentials to the user
    username = input("Please, type your username: ")
    password = input("Please, type the password: ")
    #Asking credentials to the user again avoiding empty values
    while username == "" or password == "":
        print("Be careful! Empty files are not allowed.")
        username = input("Please, type your username: ")
        password = input("Please, type the password: ")
    #Comparing the password stored in the data storage with the password typed to the user
    validate = verify_credentials(username, password)
    #The function verify_credentials returns a boolean. If it's True, will confirm that the credentials are
    #correct, otherwise, will say that the credentials are incorrect.
    if validate:
        return True
    else:
        return False