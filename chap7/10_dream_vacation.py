dream_vacations = []

while True:
    vacation = input("If you could visit one place in the world, where would you go? (type 'quit' to end): ")
    
    if vacation.lower() == 'quit':
        break
    
    dream_vacations.append(vacation)

print("\nPoll Results:")
for vacation in dream_vacations:
    print(f"- {vacation}")
