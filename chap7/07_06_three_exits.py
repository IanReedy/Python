"""
In this code, I set the initial age to 1 and the active variable to True. 
I create a loop that continues to run as long as the age is not 0 and the active variable is True. 
Within the loop, I ask the user to enter their age. If they input '0', I print "Exiting..." and break the loop. 
If the user is under 3 years old, I print that their ticket is free. 
For ages between 3 and 12, I print that the ticket costs $10. 
For anyone older than 12, I print that the ticket costs $15.
"""

age = 1  
active = True  

while age != 0 and active:  
    age = int(input("Enter your age (or 0 to quit): "))

    if age == 0:
        print("Exiting...")
        break  
    elif age < 3:
        print("Ticket is free.")
    elif age <= 12:
        print("Ticket is $10.")
    else:
        print("Ticket is $15.")
