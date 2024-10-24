"""
I create a list called `nums` using a list comprehension that contains the cubes of the numbers from 1 to 10. 
Then, I print the first three items in the list, three items from the middle, and the last three items using slicing.
"""

nums = [value**3 for value in range(1,11)]
print("The first three items in the list are:", nums[:3])
print("Three items from the middle of the list are:", nums[3:6])
print("The last three items in the list are:", nums[-3:])