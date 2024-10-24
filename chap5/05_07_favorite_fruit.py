"""
I create a set called `favorite_fruits` containing 'apple', 'orange', and 'grapes'. 
Then, I check if certain fruits are in the set using the `__contains__` method. 
If 'apple' is found, I print a message indicating that apples are good. 
If 'banana' is found, I print a dismissive message. 
Next, I check for 'orange', and if present, I print that oranges are my favorite. 
I continue checking for 'grapes', printing that they are mediocre, and finally check for 'watermelon', again printing a dismissive message if it were found.
"""

favorite_fruits = {'apple','orange','grapes'}

if favorite_fruits.__contains__('apple'):
    print('Apples are pretty good')
elif favorite_fruits.__contains__('bananna'):
    print('ew')
elif favorite_fruits.__contains__('orange'):
    print('Oranges are my favorite')
elif favorite_fruits.__contains__('grapes'):
    print('Grapes are medicore')
elif favorite_fruits.__contains__('watermelon'):
    print('ew')