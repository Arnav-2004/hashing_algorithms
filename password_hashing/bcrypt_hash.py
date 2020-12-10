# Importing the hashing algorithm
import bcrypt

# Defining the password (Note: Using byte format)
passwd = b'Password'

# Hashing the password
hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())

# Printing the hashed password
# print(hashed)

# Changing the password to check the functioning of the below statements
# passwd = b'Changed'

# Checking if original password and hashed password matches or not
if bcrypt.checkpw(passwd, hashed):
    print('Password is correct!')
else:
    print('Password is incorrect!')

# Workfactor

import time

start = time.time()
# By default the work factor (rounds) is 12
# Recommended : 12 (as it ramps up pretty quickly)
# This might depend on what you are trying to achieve and how powerful is your server
hashed = bcrypt.hashpw(passwd, bcrypt.gensalt(rounds=14))
stop = time.time()

print(stop - start)


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