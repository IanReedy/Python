"""
I create a dictionary called `rivers` to map river names to the countries they flow through. 
I populate the dictionary with entries for the Nile, Amazon, and Yangtze rivers, associating each with its corresponding country. 
Then, I use a for loop to print a statement for each river and the country it runs through. 
Finally, I print a list of the countries by iterating through the dictionary again.
"""

rivers = {}
rivers['Nile'] = 'Egypt'
rivers['Amazon'] = 'Brazil'
rivers['Yangtze'] = 'China'

for river in rivers:
    print(f"The {river} runs through {rivers[river]}.")

print("\nCountries:")
for river in rivers:
    print(rivers[river])
