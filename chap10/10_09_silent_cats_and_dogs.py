#3
filenames = ['/Users/ianreedy/Desktop/Python/chap10/cats.txt', '/Users/ianreedy/Desktop/Python/chap10/dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        pass
