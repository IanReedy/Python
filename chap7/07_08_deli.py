"""
In this code, I start with a list of sandwich orders and an empty list to hold finished sandwiches. 
I use a while loop that continues as long as there are sandwich orders left. 
Within the loop, I pop a sandwich from the end of the orders list, print a message indicating that I've made that sandwich, 
and then add it to the finished sandwiches list. 
After all sandwiches have been made, I print a summary of all the sandwiches that were finished.
"""

sandwich_orders = ['tuna', 'ham', 'turkey', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")
