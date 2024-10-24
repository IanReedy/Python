"""
I create three dictionaries, `person1`, `person2`, and `person3`, to store information about individuals, including their names, ages, and cities. 
I then compile these dictionaries into a list called `people`. 
Finally, I use a for loop to iterate through the list, printing each person's details in a formatted string.
"""

person1 = {}
person1['name'] = 'Sam'
person1['age'] = 19
person1['city'] = 'New York'

person2 = {}
person2['name'] = 'Colin'
person2['age'] = 19
person2['city'] = 'Los Angeles'

person3 = {}
person3['name'] = 'Dennis'
person3['age'] = 18
person3['city'] = 'Chicago'

people = [person1, person2, person3]

for person in people:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}\n")
