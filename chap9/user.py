# This module defines a basic User class with user information and greeting methods.

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("User Information:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("Location:", self.location)

    def greet_user(self):
        print("Hello,", self.first_name, self.last_name + "!")
