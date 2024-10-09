rivers = {}
rivers['Nile'] = 'Egypt'
rivers['Amazon'] = 'Brazil'
rivers['Yangtze'] = 'China'

for river in rivers:
    print(f"The {river} runs through {rivers[river]}.")

print("\nCountries:")
for river in rivers:
    print(rivers[river])
