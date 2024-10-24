"""
I create a dictionary called `fav_number` to store favorite numbers associated with different names. 
I add entries for several individuals along with their corresponding favorite numbers. 
Then, I use a for loop to iterate through the dictionary, printing each person's name and their favorite number in a formatted string.
"""

fav_number = {}

fav_number['Dennis'] = 3
fav_number['Sam'] = 6
fav_number['Colin'] = 9
fav_number['Tyler'] = 12
fav_number['Nick'] = 15 

for x in fav_number:
    print(x + "'s favorite number is " + str(fav_number[x]))
