#5
filename = '/Users/ianreedy/Desktop/Python/chap10/your_text_file.txt'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read().lower()
        count_the = contents.count('the')
        count_the_space = contents.count('the ')
        
        print(f"Occurrences of 'the': {count_the}")
        print(f"Occurrences of 'the ' (with space): {count_the_space}")
except FileNotFoundError:
    print(f"Sorry, {filename} is missing.")
