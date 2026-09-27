import bcrypt
#Calling the function for extracting the info of the user from the data storage file.
from CRUD import *

#Authentication function that will validate the credentials.
def verify_credentials(username:str, password:str) -> bool: 
    users = watch_users()
    #Conditional to validate if we find users
    if users:
        #Validating if the user exists in the data storage file.
        for x, obj in users.items():
            #If exists, break the flow returning the message.
            if obj["user"] == username:
                checkValidation = bcrypt.checkpw(password.encode('utf-8'), obj["password"].encode('utf-8'))
                if checkValidation:
                    return True
                else:
                    return False
    else:
        return False
