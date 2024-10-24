"""
I create a dictionary called `glossary` to store programming terms and their definitions. 
I populate the dictionary with several terms, each associated with a concise description. 
Then, I use a for loop to iterate through each term and its meaning, printing them in a formatted way with each definition on a new line.
"""

glossary = {}
glossary['Variable'] = 'Stores a value.'
glossary['Function'] = 'Reuses code to perform a task.'
glossary['Loop'] = 'Repeats code multiple times.'
glossary['List'] = 'A collection of items.'
glossary['Dictionary'] = 'Key-value pairs of data.'
glossary['String'] = 'A sequence of characters.'
glossary['Integer'] = 'A whole number without a decimal.'
glossary['Float'] = 'A number that can have decimals.'
glossary['Boolean'] = 'A type that represents True or False.'
glossary['Tuple'] = 'An immutable list of items.'

for term, meaning in glossary.items():
    print(term + ": " + meaning + "\n")
