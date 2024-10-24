"""
I create a list called `nums` using a list comprehension that contains the cubes of the numbers from 1 to 10. 
Then, I print the entire list, which shows the cubic values of each number.
"""
nums = [value**3 for value in range(1,11)]
print(nums)