filename = '/Users/ianreedy/Desktop/Python/chap10/guest.txt'

name = input("Enter your name: ")

with open(filename, 'w') as file:
    file.write(name)
