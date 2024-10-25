"""
This code defines a function that formats and returns a string with a city and its country, 
and calls the function with three city-country pairs.
"""

def city_country(city, country):
    return f"{city}, {country}"

print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("Paris", "France"))
