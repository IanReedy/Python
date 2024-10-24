"""
In this code, I ask the user how many people they will be inviting to dinner 
and convert their input from a string to an integer. 
Then, I check if the number of people is greater than 8. 
If it is, I inform them that they will have to wait for a table. 
Otherwise, I let them know that their table is ready and to follow me.
"""

people = input("How many people will you be inviting to dinner? ")
people = int(people)

if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready, follow me.")