cities = {}
cities['New York'] = {}
cities['New York']['country'] = 'USA'
cities['New York']['population'] = 8419600
cities['New York']['fact'] = 'The city that never sleeps.'

cities['Los Angeles'] = {}
cities['Los Angeles']['country'] = 'USA'
cities['Los Angeles']['population'] = 3980400
cities['Los Angeles']['fact'] = 'Known for Hollywood.'

cities['Chicago'] = {}
cities['Chicago']['country'] = 'USA'
cities['Chicago']['population'] = 2716000
cities['Chicago']['fact'] = 'Famous for its deep-dish pizza.'

for city in cities:
    country = cities[city]['country']
    population = cities[city]['population']
    fact = cities[city]['fact']
    print(city + ": Country - " + country + ", Population - " + str(population) + ", Fact - " + fact + "\n")
