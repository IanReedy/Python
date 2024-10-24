"""
In this code, I create a dictionary to store information about three cities: New York, Los Angeles, and Chicago. 
For each city, I include details such as the country, population, and a fun fact. 
I then loop through the dictionary to print this information in a readable format. 
After that, I add a landmark for each city and print all the details again, 
including the new information about the landmarks.
"""

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

cities['New York']['landmark'] = 'Empire State Building'
cities['Los Angeles']['landmark'] = 'Hollywood Sign'
cities['Chicago']['landmark'] = 'Willis Tower'

for city in cities:
    country = cities[city]['country']
    population = cities[city]['population']
    fact = cities[city]['fact']
    landmark = cities[city]['landmark']
    print(city + ": Country - " + country + ", Population - " + str(population) + ", Fact - " + fact + ", Landmark - " + landmark + "\n")
