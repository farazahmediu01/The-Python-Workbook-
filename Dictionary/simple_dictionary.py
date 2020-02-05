faraz = {'name': 'faraz', 'age': '22', 'education': 'bachlers',
         'color': 'brown', 'passion': 'learning'}
space = ' '
count = 1

faraz['destiny'] = 'data scientist'
faraz['food'] = 'meal'
faraz['experience'] = 'one year'

print(faraz)

print('\nKeys\t\t<->\tValues\n')


for key in faraz:
    # this if block runs when the lenght of key is smaller then 9.
    if len(key) < 9:
        # this variable stores the number of characters in key.
        str_len = len(key)
        # this is the measurement of how many spaces are required to reached the lenght of 9 charachters.
        str_len = 9 - str_len
        space_added = key + space * str_len   # putting require spaces in key.
    else:
        # if lenght of key is more then 9 we don't alter it.
        space_added = key

    if key:
        print(f'{count}){space_added.title()}\t:\t{faraz[key].title()}')

    count += 1
print("lenght of dictionary =", len(faraz))
