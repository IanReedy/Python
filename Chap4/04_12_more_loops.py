"""
I create a list called `my_foods` containing 'pizza', 'falafel', and 'carrot cake', and then create a copy of this list called `friend_foods`. 
I add 'cannoli' to `my_foods` and 'ice cream' to `friend_foods`. 
I print my favorite foods by iterating over `my_foods` and print my friend's favorite foods by iterating over `friend_foods`, capitalizing each food name.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food.title())
print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food.title())