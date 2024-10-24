"""
In this code, I create a loop that continuously prompts the user to enter a pizza topping. 
After each topping is entered, I print a message confirming that the topping will be added to the pizza. 
If the user types 'quit', the loop will break, and the program will stop asking for more toppings.
"""

while True:
    topping = input("Enter a topping (or 'quit' to finish): ")
    print("We will add " + topping + " to your pizza.")

    if topping == 'quit':
        break
