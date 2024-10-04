favorite_numbers = {}
favorite_numbers['Sam'] = [3, 7, 21]
favorite_numbers['Colin'] = [5, 10]
favorite_numbers['Dennis'] = [8, 14, 22]

for person, numbers in favorite_numbers.items():
    number_strings = []
    for number in numbers:
        number_strings.append(str(number))
    print(person + "'s favorite numbers: " + ', '.join(number_strings) + "\n")
