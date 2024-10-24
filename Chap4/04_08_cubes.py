"""
I create a list called `nums` containing the numbers from 1 to 10 using `range()`. 
Then, I use a for loop to iterate over each number in the list and print the cube of each number (num raised to the power of 3).
"""

nums = list(range(1,11))
for num in nums:
    print(num**3)