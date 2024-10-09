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
