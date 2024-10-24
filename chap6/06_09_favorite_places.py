"""
I create a dictionary called `favorite_places` to store each person's name along with a list of their favorite locations. 
For Dennis, Colin, and Sam, I specify their respective favorite places. 
Then, I use a for loop to iterate through the dictionary, printing each person's name along with their favorite places in a formatted string, using `join` to list the places.
"""

favorite_places = {}
favorite_places['Dennis'] = ['Central Park', 'Statue of Liberty']
favorite_places['Colin'] = ['Griffith Park', 'Santa Monica Beach']
favorite_places['Sam'] = ['Millennium Park', 'Navy Pier']

for person, places in favorite_places.items():
    print(f"{person}'s favorite places: {', '.join(places)}\n")
