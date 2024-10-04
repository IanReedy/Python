favorite_places = {}
favorite_places['Dennis'] = ['Central Park', 'Statue of Liberty']
favorite_places['Colin'] = ['Griffith Park', 'Santa Monica Beach']
favorite_places['Sam'] = ['Millennium Park', 'Navy Pier']

for person, places in favorite_places.items():
    print(f"{person}'s favorite places: {', '.join(places)}\n")
