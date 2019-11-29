'''
def removing_outliers(array,inp):
    dup_array = array.sort()

    for i in range(inp):                               # dup_array[:inp]:
        del dup_array[i]                               #dup_array.pop(i)    
    dup_array.reverse()
    
    for i in range(inp):                               # dup_array[:inp]:
        del dup_array[i]                               #dup_array.pop()
    dup_array.reverse()

    return dup_array
'''
array = []
dup_array = []
n = 0
inp = input('Enter values: ')

while inp!='':
    try:
        inp = int(inp)
    except:
        continue

    array.append(inp)
    inp = input('Enter values (press enter to exit): ')

print()
inp = int(input('Enter number for removing outliers from list: '))
array.sort()
for i in array:
    dup_array.append(i)

#removing_outliers(array,inp)
for i in range(1, inp+1):
    dup_array.pop(i)
    dup_array.pop(-i)


print(f"Original Array    = {array}.")
print(f'Removed Outlayers = {dup_array}')
