"""
This file demonstrates various import methods for the greet_user function.
"""

# Importing the entire module
import my_functions
my_functions.greet_user("Alice")

# Importing the specific function
from my_functions import greet_user
greet_user("Bob")

# Importing the function with an alias
from my_functions import greet_user as fn
fn("Charlie")

# Importing the entire module with an alias
import my_functions as mn
mn.greet_user("Diana")

# Importing all functions from the module
from my_functions import *
greet_user("Eve")
