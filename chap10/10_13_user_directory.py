import json

user_info = {
    "username": input("Enter your username: "),
    "age": input("Enter your age: "),
    "location": input("Enter your location: ")
}

filename = '/Users/ianreedy/Desktop/Python/chap10/user_info.json'
with open(filename, 'w') as file:
    json.dump(user_info, file)

with open(filename) as file:
    loaded_user_info = json.load(file)
    print("Here's what I remember about you:")
    for key, value in loaded_user_info.items():
        print(f"{key.title()}: {value}")
