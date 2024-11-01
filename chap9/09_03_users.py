# This code defines a User class with methods to display user information and greet the user personally.

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

user1 = User("Alice", "Smith", 30, "New York")
user2 = User("Bob", "Johnson", 25, "Chicago")
user3 = User("Charlie", "Brown", 35, "Los Angeles")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
