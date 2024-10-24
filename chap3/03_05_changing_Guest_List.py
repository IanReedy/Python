"""
I create a list called `people` containing the names 'Geroge Washington, ', 'Abe Lincoln ', and 'Michael Jackson'. 
Then, I print the entire list. After that, I access the third element in the list (index 2) and print a message stating that "Michael Jackson won't be able to make it." 
Next, I remove 'Michael Jackson' from the list and insert 'Michael Jordan' at index 2. Finally, I print the updated list.
"""

people = ['Geroge Washington, ', 'Abe Lincoln ', 'Michael Jackson']
print(people)

print(people[2] + " won't be able to make it.") 

people.remove('Michael Jackson')
people.insert(2,'Michael Jordan')

print(people)