"""
I create a list called `people` with 'Geroge Washington, ', 'Abe Lincoln ', and 'Michael Jackson'. 
After printing the list, I mention that "Michael Jackson won't be able to make it," remove him, and insert 'Michael Jordan' at index 2. 
I announce that a bigger table allows me to invite more people and add 'Barack Obama', 'Albert Einstein', and 'Martin Luther King Jr.'. 
Then, I state that I can only invite 2 people now, so I remove the last four names with `pop()`. 
Finally, I print the remaining guests still invited to the party.
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
people.insert(4,'Martin Luther King Jr.')

print(people) 

print("Unfortunately the bigger table won't be ready in time and now and can only invite 2 people")

people.pop() 
people.pop()
people.pop() 
people.pop()

print(f"{people} are still invited to the party")
