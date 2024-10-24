"""
I assign the string 'python_notes.txt' to the variable `filename`. 
Then, I use the `removesuffix()` method to remove the '.txt' suffix from `filename`, resulting in 'python_notes'. 
If the '.txt' suffix is removed from the filename, the code will still work, but it would not perform the intended removal if the string doesn't end with '.txt'.
"""


filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
#if '.txt is removed the code will not work