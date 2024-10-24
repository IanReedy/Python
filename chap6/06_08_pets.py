"""
I create three dictionaries, `pet1`, `pet2`, and `pet3`, to store information about pet owners and their animals. 
Each dictionary includes the owner's name and the type of pet they have. 
I compile these dictionaries into a list called `pets`, and then use a for loop to iterate through the list, printing each owner's name along with their pet's type in a formatted string.
"""

pet1 = {}
pet1['owner'] = 'Sam'
pet1['animal'] = 'Dog'

pet2 = {}
pet2['owner'] = 'Colin'
pet2['animal'] = 'Cat'

pet3 = {}
pet3['owner'] = 'Dennis'
pet3['animal'] = 'Parrot'

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Owner: {pet['owner']}, Pet: {pet['animal']}\n")
