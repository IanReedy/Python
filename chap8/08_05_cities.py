"""
This code defines a function that describes a city and its country, 
with a default country value, and calls the function for three different cities.
"""

def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik")
describe_city("Oslo", "Norway")
describe_city("Stockholm", "Sweden")
