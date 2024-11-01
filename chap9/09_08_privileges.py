# This code defines a Privileges class used within an Admin class to show specific admin privileges.

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

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin Privileges:", ", ".join(self.privileges))

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

admin = Admin("Alice", "Smith", 30, "New York")
admin.privileges.show_privileges()
