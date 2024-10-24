"""
In this code, I create a loop that asks the user to enter their age. If the user inputs '0', the loop will break, and the program will stop running. 
If the user is under 3 years old, I print that their ticket is free. 
For ages between 3 and 12, I print that the ticket costs $10. 
For anyone older than 12, I print that the ticket costs $15.
"""

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
