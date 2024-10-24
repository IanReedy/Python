"""
I create an empty dictionary called `glossary` to store programming terms and their definitions. 
I add several terms along with their corresponding definitions to the dictionary. 
Then, I use a for loop to iterate through each term in the glossary, printing the term followed by its definition, each on a new line.
"""

glossary = {}

glossary["concatenate"] = 'link (things) together in a chain or series.'
glossary['int'] = 'used to define a variable as a certain number.'
glossary['Variable'] = "A named location in memory used to store a value."
glossary['Function'] = "A block of reusable code that performs a specific task."
glossary['Loop'] = "A control structure that repeats a block of code multiple times."

for term in glossary:
    print(term + ": " + glossary[term] + "\n")