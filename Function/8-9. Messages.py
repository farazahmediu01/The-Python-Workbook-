def shortest_lenght(series):
    lenght_of_element = None
    for element in series:
        if lenght_of_element is None:
            lenght_of_element = len(element)
        if lenght_of_element >= len(element):
            lenght_of_element = len(element)


def sort_list(short_list_of_messages):
    sorted_list_of_messages = []
    lenght = None
    index = 0
    while short_text_messages:
        if lenght_of_element is None:
            lenght_of_element = len(element)
        if lenght_of_element >= len(element):
            lenght_of_element = len(element)

    def show_messages(messages):
    print(f"\nBlow is the list of messages.")
    if messages:
        for message in messages:
            print(message.title())


def send_message(messages, sent_message):
    while messages:
        current_message = messages.pop()
        print("'" + current_message + "'" + "\t is sending...")
        sent_message.append(current_message)


# The List messages contains a series of short text messages.
short_text_messages = ['hello', 'how are you doing', 'what\'s going on?',
                       'how was the day', 'see you soon', 'thanks me later',
                       'i\'ll busy right now call me later', 'Thank you so much',
                       'good bye']
# This list contain the messages which has been sent.
sent_message = []
print(messages)
print(sent_message)

# send_message(messages, sent_message)
# show_messages(messages)
# show_messages(sent_message)
