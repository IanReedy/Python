#6
import json

def get_stored_username():
    filename = '/Users/ianreedy/Desktop/Python/chap10/username.json'
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("Enter your username: ")
    with open('/Users/ianreedy/Desktop/Python/chap10/username.json', 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct_user = input(f"Are you {username}? (yes/no): ")
        if correct_user.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you for next time, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you for next time, {username}!")

greet_user()
