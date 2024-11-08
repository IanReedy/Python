#2
import json

favorite_number = input("What's your favorite number? ")
with open('/Users/ianreedy/Desktop/Python/chap10/favorite_number.json', 'w') as file:
    json.dump(favorite_number, file)
