def sorting_list(serires):
    # Fetch element
    # Find lenght
    # Put the lenght as a key and value as element.

    dic = {}
    lenght_of_element = None
    for element in serires:
        if lenght_of_element is None:
            lenght_of_element = len(element)
        else:
            lenght_of_element = len(element)
        dic[lenght_of_element] = element

    return dic


def dic_to_list(dictionary):#, sorted_text_messages):
    for i in sorted(dictionary):
        # print(i, '=', apni_dictetionary[i])
        sorted_text_messages.append(dictionary[i])

    return sorted_text_messages


# The List messages contains a series of short text messages.
text_messages = ['hello', 'how are you doing', 'what\'s going on?',
                 'how was the day', 'see you soon', 'thanks me later',
                 'i\'ll busy right now call me later', 'Thank you so much',
                 'good bye']
sorted_text_messages = []


sorted_dictionary = sorting_list(text_messages)
sorted_text_message = dic_to_list(sorted_dictionary)#,sorted_text_messages)

for i in text_messages:
    print(i)
print()

for i in sorted_text_messages:
    print(i)
