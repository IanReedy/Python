"""
I create a list called `current_users` with existing usernames and a list called `new_users` with usernames that are being requested. 
I generate a new list, `current_users_lower`, which contains all usernames from `current_users` converted to lowercase for case-insensitive comparison. 
Then, I loop through each `new_user` in `new_users` and check if their lowercase version is in `current_users_lower`. 
If it is, I print a message indicating that the username is already taken; otherwise, I print that the username is available.
"""

current_users = ['Admin', 'Sam', 'Colin', 'Dennis', 'Cooper']
new_users = ['Admin', 'Liam', 'Olivia', 'Dennis', 'Noah']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available!")
