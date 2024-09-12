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
