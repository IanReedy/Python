# This file imports the Admin class from user_module and creates an Admin instance to show privileges.

from user_module import Admin

admin = Admin("Alice", "Smith", 30, "New York")
admin.privileges.show_privileges()
