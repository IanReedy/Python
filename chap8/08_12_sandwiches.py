"""
This code defines a function that accepts a variable number of sandwich items, 
prints a summary of the sandwich order, and demonstrates the function with three 
calls, each using a different number of arguments.
"""

def make_sandwich(*items):
    print("Sandwich order includes:")
    for item in items:
        print(f"- {item}")

make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("ham", "cheese")
make_sandwich("roast beef", "onions", "pickles", "mustard")
