"""
This code defines a function that takes a list of text messages 
and prints each message when called.
"""

def show_messages(messages):
    for message in messages:
        print(message)

text_messages = [
    "Hello, how are you?",
    "Don't forget the meeting at 3 PM.",
    "Happy Birthday!",
    "Let's grab lunch tomorrow."
]

show_messages(text_messages)
