"""
This program builds a user profile with key information.
"""

def build_profile(first_name, last_name, **additional_info):
    """Build a dictionary containing user profile information."""
    profile = {
        'first_name': first_name,
        'last_name': last_name
    }
    
    for key, value in additional_info.items():
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


"""
This program sends messages and tracks sent messages.
"""

def send_messages(messages):
    """Print each message and move it to the sent_messages list."""
    sent_messages = []
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
    
    return sent_messages


text_messages = [
    "Hello, how are you?",
    "Don't forget the meeting at 3 PM.",
    "Happy Birthday!",
    "Let's grab lunch tomorrow."
]


sent_messages = send_messages(text_messages[:])
print("Sent messages:", sent_messages)
print("Remaining messages:", text_messages) 


"""
This program summarizes sandwich orders based on user input.
"""

def make_sandwich(*ingredients):
    """Print a summary of the sandwich order."""
    print("Sandwich order includes:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("ham", "cheese")
make_sandwich("roast beef", "onions", "pickles", "mustard")

