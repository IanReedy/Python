"""
I create a list called `locations` containing 'Paris', 'Germany', 'Switzerland', and 'Ireland'. 
I print the original list, reverse it, and print the reversed list. 
Then, I display the sorted version of the list and print the total number of locations. 
I insert 'Idaho' at the beginning of the list, print the updated list, and remove the last location using `pop()`, printing the list again. 
Next, I remove 'Idaho' and print the list once more, then append 'Florida' to the end of the list and print the final version.
"""

locations = ['Paris','Germany','Switzerland','Ireland']
print(locations)
locations.reverse()
print(locations)
print(sorted(locations))
print("They're " + str(len(locations)) + " locations on this list.")
locations.insert(0,'Idaho')
print(locations)
locations.pop()
print(locations)
locations.remove('Idaho')
print(locations)
locations.append('Florida')
print(locations)