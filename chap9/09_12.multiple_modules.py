# This file imports the Admin class from admin_module and creates an instance to show privileges.

from admin_module import Admin

admin = Admin("Alice", "Smith", 30, "New York")
admin.privileges.show_privileges()
