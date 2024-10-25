"""
This code builds on the previous exercise by ensuring that the original list of messages 
remains unchanged after calling the send_messages() function. It uses a copy of the list 
to send messages and then prints both lists to verify the original messages are intact.
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
print("Original messages:", text_messages)  
