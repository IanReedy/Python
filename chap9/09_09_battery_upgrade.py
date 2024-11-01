# This code defines an ElectricCar class with a Battery class inside it, with an upgrade method to increase battery capacity.

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print("Battery size:", self.battery_size, "-kWh")

    def get_range(self):
        range = 240 if self.battery_size == 40 else 400 if self.battery_size == 65 else 0
        print("This car can go about", range, "miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

car = ElectricCar("Tesla", "Model S", 2024)
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()
