"""
I create a list called `people_to_poll` containing names of individuals I want to survey. 
I also create a dictionary called `people_who_poll` to track who has already responded, marking Alice and David as respondents. 
Then, I use a for loop to iterate through `people_to_poll`, checking if each person has responded. 
If they have, I print a thank-you message; if they haven't, I prompt them to take the poll.
"""

people_to_poll = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

people_who_poll = {}
people_who_poll['Alice'] = True
people_who_poll['David'] = True

for person in people_to_poll:
    if person in people_who_poll:
        print(f"Thank you, {person}, for responding!")
    else:
        print(f"{person}, please take the poll!")
