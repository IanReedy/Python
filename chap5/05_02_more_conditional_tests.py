"""
I assign the string 'apple' to the variable `fruit` and print predictions and evaluations for comparisons involving `fruit`. 
Next, I assign the string 'HELLO' to the variable `word` and print predictions and evaluations for case-insensitive comparisons. 
Then, I create two variables, `num1` and `num2`, with values 5 and 10, respectively, and print predictions and evaluations for various numerical comparisons. 
I check both logical conditions using `and` and `or` operators for `num1` and `num2`. 
Finally, I create a list called `my_list` containing numbers 1 to 5 and print predictions and evaluations for membership checks within the list, using `in` and `not in` operators.
"""

fruit = "apple"
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')



word = "HELLO"
print("\nIs word.lower() == 'hello'? I predict True.")
print(word.lower() == 'hello')

print("\nIs word.lower() == 'HELLO'? I predict False.")
print(word.lower() == 'HELLO')



num1 = 5
num2 = 10

print("\nIs num1 > 3? I predict True.")
print(num1 > 3)

print("\nIs num1 < num2? I predict True.")
print(num1 < num2)

print("\nIs num1 >= 5? I predict True.")
print(num1 >= 5)

print("\nIs num1 <= 3? I predict False.")
print(num1 <= 3)



print("\nIs num1 > 3 and num2 > 8? I predict True.")
print(num1 > 3 and num2 > 8)

print("\nIs num1 > 10 or num2 > 8? I predict True.")
print(num1 > 10 or num2 > 8)



my_list = [1, 2, 3, 4, 5]
print("\nIs 3 in my_list? I predict True.")
print(3 in my_list)

print("\nIs 10 in my_list? I predict False.")
print(10 in my_list)



print("\nIs 10 not in my_list? I predict True.")
print(10 not in my_list)

print("\nIs 3 not in my_list? I predict False.")
print(3 not in my_list)
