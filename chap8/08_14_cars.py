"""
This code defines a function that creates a dictionary containing information about a car, 
including manufacturer, model, and additional attributes, and demonstrates its use 
with a specific car.
"""

def make_car(manufacturer, model, **features):
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for key, value in features.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
