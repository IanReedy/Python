"""
I create a list called `numbers` containing the integers from 1 to 9. 
Then, I use a for loop to iterate through each number in the list. 
I check the value of each number to determine its ordinal suffix: 
- If it's 1, I print it with 'st', 
- If it's 2, I print it with 'nd', 
- If it's 3, I print it with 'rd', 
- For all other numbers, I print it with 'th'.
"""

numbers = list(range(1, 10))

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
