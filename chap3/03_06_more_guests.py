"""
I create a list called `people` containing 'Geroge Washington, ', 'Abe Lincoln ', and 'Michael Jackson'. 
Then, I print the entire list and follow up by printing a message that "Michael Jackson won't be able to make it." 
I remove 'Michael Jackson' from the list and insert 'Michael Jordan' at index 2. After printing the updated list, I announce that a bigger table has been found to invite more people. 
I then insert 'Barack Obama' at the beginning, 'Albert Einstein' at index 2, and append 'Martin Luther King Jr.' to the end of the list before printing the final updated list.
"""

people = ['Geroge Washington, ', 'Abe Lincoln ', 'Michael Jackson']
print(people)

print(people[2] + " won't be able to make it.") 

people.remove('Michael Jackson')
people.insert(2,'Michael Jordan')

print(people)

print("A bigger table has been found I can invite more people")

people.insert(0,'Barack Obama')
people.insert(2,'Albert Einstein')
people.append('Martin Luther King Jr.')

print(people)