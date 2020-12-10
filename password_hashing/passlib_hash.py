# Importing the hashing algorithm
from passlib.hash import sha256_crypt

# Defining the password
passwd = 'Password'

# Hashing the password
hashed = sha256_crypt.hash(passwd)

# Printing the hashed password
# print(hashed)

# Changing the password to check the functioning of the below statements
# passwd = 'Changed'

# Checking if original password and hashed password matches or not
if sha256_crypt.verify(passwd, hashed):
    print('Password is correct!')
else:
    print('Password is incorrect!')


# This can be easily implemented with database

'''
Step 1. Check if the username exist in the database and if the user exist move ahead to step 2

Step 2. Then hash the password (remember the format should be utf-8) associated with that username
using the above logic and move ahead to step 3

Step 3. Match the password entered by the user and the hashed password
and if it matches move ahead to step 4 otherwise to step 5

Step 4. Redirect the user wherever you want

Step 5. Give a warning message to the user
'''