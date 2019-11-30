words = []

print('\nPlease enter serires of words (press enter to quit).')
inp = input('> ')

while inp!='':
    words.append(inp)
    inp = input('> ')

print(f'\nOriginal = {words}')
print(f'Modified = {list(set(words))}')
