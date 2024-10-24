"""
In this code, I prompt the user to input their desired type of rental car. 
I then convert their input to a string, although it is already in string format. 
Finally, I print a message indicating that I will check for availability of the specified car type, 
capitalizing the first letter of each word for a nicer presentation.
"""

car = input("What type of rental car would you like? ")
car = str(car)

print(f"Let me see if I can find you a {car.title()}.")