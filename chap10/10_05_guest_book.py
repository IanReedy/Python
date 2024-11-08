#34
filename = '/Users/ianreedy/Desktop/Python/chap10/guest_book.txt'

while True:
    name = input("Enter your name (or type 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    with open(filename, 'a') as file:
        file.write(name + '\n')
        print(f"Hello, {name}. Your name has been added to the guest book.")
