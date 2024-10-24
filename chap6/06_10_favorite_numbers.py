"""
I create a dictionary called `favorite_numbers` that maps each person's name to a list of their favorite numbers. 
For Sam, Colin, and Dennis, I specify their respective favorite numbers as lists. 
Then, I use a for loop to iterate through the dictionary. 
Within the loop, I convert each number to a string and append it to a new list called `number_strings`. 
Finally, I print each person's name along with their favorite numbers, formatted as a comma-separated string.
"""

favorite_numbers = {}
favorite_numbers['Sam'] = [3, 7, 21]
favorite_numbers['Colin'] = [5, 10]
favorite_numbers['Dennis'] = [8, 14, 22]

for person, numbers in favorite_numbers.items():
    number_strings = []
    for number in numbers:
        number_strings.append(str(number))
    print(person + "'s favorite numbers: " + ', '.join(number_strings) + "\n")
