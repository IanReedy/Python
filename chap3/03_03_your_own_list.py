"""
I create a list of transport brands called `transports`, containing 'honda', 'nissan', and 'ford'. 
Then, I use a for loop to iterate over each brand in the list. For each brand, I check if it matches a specific name and print a corresponding message.
"""


transports = ['honda', 'nissan', 'ford']
for transport in transports:
    if transport == 'honda':
        print("I own a " + transport.title() + " Civic.")
    if transport == "nissan":
        print(transport.title() + "s are kinda ugly.")
    if transport == 'ford':
        print(transport.title() + "s are also pretty ugly.")
