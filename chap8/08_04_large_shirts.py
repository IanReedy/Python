"""
This code defines a function that defaults to a large shirt with the message 'I love Python' 
and demonstrates creating shirts of different sizes and messages.
"""

def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message is '{message}'.")

make_shirt()
make_shirt("Medium")
make_shirt("Small", "Code is life")
