integers = []
sorted_list = []
pos_index = 0
neg_index = 0
zero_index = 0

print('\nEnter integer only (blank line to quit).')
integer = input('> ')

while integer != '':
    try:
        integer = int(integer)
    except:
        print('Wrong input')
        continue
    
    integers.append(integer)
    integer = input('> ')

# Sorting list as per the requirements.
for index in range(len(integers)):    
    if integers[index] < 0:
        sorted_list.insert(neg_index, integer[index])
        neg_index = neg_index + 1

    elif integers[index] == 0:
        sorted_list.insert(zero_index, integer[index])
        zero_index = neg_index + zero_index + 1
    
    elif integers[index] > 0:
        sorted_list.insert(pos_index,integers[index])
        pos_index = neg_index + zero_index + pos_index + 1
                                                                                                               #if integer[index] > 0: sorted_list.append(integer[index])

print(f'The list in sorted order:\n{integers}')