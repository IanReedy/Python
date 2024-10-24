"""
In this code, I start with a list of sandwich orders that includes several 'pastrami' sandwiches. 
I first print a message to indicate that the deli has run out of pastrami. 
Then, I use a while loop to remove all instances of 'pastrami' from the sandwich orders list. 
After that, I iterate through the remaining sandwich orders, print a message for each one indicating that it has been made, 
and add it to the list of finished sandwiches. 
Finally, I print a summary of all the sandwiches that were completed.
"""

sandwich_orders = ['tuna', 'ham', 'turkey', 'veggie', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
