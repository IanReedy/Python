"""
In this code, I prompt the user to enter a number and convert their input from a string to an integer. 
Then, I check if the number is a multiple of 10 by using the modulus operator. 
If the remainder when dividing the number by 10 is 0, I print that the number is a multiple of 10. 
Otherwise, I inform the user that the number is not a multiple of 10.
"""

number = input("Enter a number ")
number = int(number)

if number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")