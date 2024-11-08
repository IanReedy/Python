import json

filename = '/Users/ianreedy/Desktop/Python/chap10/favorite_number.json'

try:
    with open(filename) as file:
        favorite_number = json.load(file)
    print(f"I know your favorite number! It's {favorite_number}.")
except FileNotFoundError:
    favorite_number = input("What's your favorite number? ")
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
