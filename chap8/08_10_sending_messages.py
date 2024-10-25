"""
This code defines a function that prints each text message from a list 
and moves each message to a new list called sent_messages. After calling 
the function, both the original and sent messages lists are printed to verify 
the transfer.
"""

def send_messages(messages):
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
