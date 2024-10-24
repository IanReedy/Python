"""
I create a list called `pizzas` containing 'buffalo', 'pepperoni', and 'stuffed crust', and a second list called `friend_pizzas` with an additional flavor, 'pineapple'. 
I print a message indicating my favorite pizzas and use a for loop to iterate over the `pizzas` list, printing each pizza with the first letter capitalized.
"""

pizzas = ['buffalo','pepperoni','stuffed crust'] 
friend_pizzas = ['buffalo','pepperoni','stuffed crust', 'pineapple']

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza.title()) 


