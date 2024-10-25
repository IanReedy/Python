"""
This code defines a function that prints the size of a shirt and the message on it, and calls the function using both positional and keyword arguments.
"""

def make_shirt(size, message):
    print(f"The shirt size is {size} and the message is '{message}'.")

make_shirt("Large", "Hello World") 
make_shirt(size="Medium", message="Python Rocks")  
