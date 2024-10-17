while True:
    age = int(input("Enter your age (or 0 to quit): "))
    
    if age == 0:
        break
    elif age < 3:
        print("Ticket is free.")
    elif age <= 12:
        print("Ticket is $10.")
    else:
        print("Ticket is $15.")
