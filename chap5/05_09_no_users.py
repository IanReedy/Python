"""
I create a set called `names` containing 'Admin', 'Sam', 'Colin', 'Dennis', and 'Cooper'. 
I check if the set is not empty. If it contains names, I use a for loop to iterate over each name. 
If the name is 'Admin', I print a specific message for them; otherwise, I print a general greeting for each user. 
Then, I redefine `names` as an empty set. I check again if the set is not empty. 
Since it is now empty, I print a message indicating that we need to find some users.
"""

names = {'Admin', 'Sam', 'Colin', 'Dennis', 'Cooper'}
if names:
    for x in names:
        if x == 'Admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print('Hello ' + x + ', how are you doing today?')
else:
    print('We need to find some users!')
names = set()  

if names:
    for x in names:
        if x == 'Admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print('Hello ' + x + ', how are you doing today?')
else:
    print('We need to find some users!')
