import bcrypt
from CRUD import *

#Example user
user ='admin'

# Example password
password = 'passwordabc'
# Converting password to array of bytes (this is MANDATORY TO DO
#THE HASHING PROCESS.)
bytes = password.encode('utf-8')
#Generating the salt. Basically is generate the random characters for protecting the
#password.
s = bcrypt.gensalt()
#We do the hashing process, completing the protection.
h = bcrypt.hashpw(bytes, s) # Hash password

#Additional component: The JSON files can't serialize the bytes format.
#We need to send in str format to the data storage.
hashed_password = h.decode("utf-8")

#Now, we will send the information to the JSON file
print(send_user_info(user, hashed_password))