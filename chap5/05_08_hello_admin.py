"""
I create a set called `names` containing 'Admin', 'Sam', 'Colin', 'Dennis', and 'Cooper'. 
Then, I use a for loop to iterate over each name in the set. 
If the name is 'Admin', I print a specific message asking if they would like to see a status report. 
For all other names, I print a general greeting asking how they are doing today.
"""

names = {'Admin','Sam','Colin','Dennis', 'Cooper'}
for x in names:
    if x == 'Admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print('Hello ' + x + ', how are you doing today?')