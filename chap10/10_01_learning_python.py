filename ='/Users/ianreedy/Desktop/Python/chap10/learning_python.txt'

with open(filename) as file:
    contents = file.read()
    print(contents)

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())


with open(filename) as file:
    contents = file.read()
    print(contents)

with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
