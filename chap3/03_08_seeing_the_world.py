"""
I create a list called `places` containing 'Japan', 'France', 'California', and 'Greece'. 
I print the original list, then display the sorted version in alphabetical order and the sorted version in reverse order. 
Next, I print the original list again to show it remains unchanged. 
I reverse the list and print it, then reverse it back and print it again. 
Finally, I show the sorted list in alphabetical order and the sorted list in reverse order again.
"""

places = ['Japan', 'France', 'California', 'Greece']
print(places)

print(sorted(places))
print(sorted(places,reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
print(sorted(places))
print(sorted(places,reverse = True))


