"""
I create a list called `nums` containing the numbers from 1 to 999,999 using `range()`. 
Then, I use a for loop to iterate over each number in the list, but instead of printing each number, I mistakenly print the entire list `nums` during each iteration.
"""

nums = list(range(1,1000000))
for num in nums:
    print(nums)