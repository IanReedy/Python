"""
In this code, I create an empty list called `dream_vacations` to store the responses from a vacation poll. 
I use a while loop to continuously prompt users for their dream vacation destination until they type 'quit' to exit. 
When a destination is entered, I add it to the `dream_vacations` list. 
Once the loop ends, I print the poll results by iterating through the list and displaying each destination.
"""

dream_vacations = []

while True:
    vacation = input("If you could visit one place in the world, where would you go? (type 'quit' to end): ")
    
    if vacation.lower() == 'quit':
        break
    
    dream_vacations.append(vacation)

print("\nPoll Results:")
for vacation in dream_vacations:
    print(f"- {vacation}")
