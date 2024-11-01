# This code defines an IceCreamStand class that inherits from Restaurant, with a method to display flavors.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def display_flavors(self):
        print("Available flavors:", ", ".join(self.flavors))

ice_cream_stand = IceCreamStand("Sweet Treats", "Dessert")
ice_cream_stand.display_flavors()
