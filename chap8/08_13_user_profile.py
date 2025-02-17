"""
This code defines a function that builds a user profile with a first name, last name, 
and additional key-value pairs, and then creates a profile with specific information.
"""

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile(
    "Ian", 
    "Reedy", 
    location="USA", 
    hobby="gaming", 
    favorite_color="blue"
)

print(my_profile)
