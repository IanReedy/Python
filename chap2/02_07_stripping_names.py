"""
I assign the string with extra leading and trailing spaces and tabs to the variable `name`, and a similar string with more formatting to `nameFix`. 
Then, I print different variations:
- `name.lstrip()` removes leading whitespace from `name`, resulting in "Ian Reedy             ".
- `name.rstrip()` removes trailing whitespace from `name`, leaving the spaces at the beginning: "           Ian Reedy".
- `nameFix.strip()` removes both leading and trailing whitespace from `nameFix`, resulting in "Ian Reedy".
"""


name = "\t\t           Ian Reedy             "
#print(name)

nameFix = "\n\t\t\t   Ian Reedy              "
#print(nameFix)

print(name.lstrip())
print(name.rstrip())
print(nameFix.strip())