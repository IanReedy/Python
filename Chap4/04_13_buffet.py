"""
I create a tuple called `foods` containing 'pizza', 'burger', 'soup', 'fries', and 'fruit'. 
I use a for loop to iterate over the tuple and print each food item with the first letter capitalized. 
Then, I redefine the `foods` tuple with new items: 'pizza', 'pie', 'burger', 'lasagna', and 'fries', and print each item in the updated tuple in a similar manner.
"""

foods = ('pizza','burger','soup','fries','fruit')
for food in foods:
    print(food.title())

#foods.append(0,'quadruple stacked baconator')

foods = ('pizza','pie','burger','lasagna','fries')
print('\n')
for food in foods:
    print(food.title())
