''' This program is to remove duplicates in List
# Initializing an empty list.
words = []

print('\nEnter a word (blank to quit):')
word = input('> ')

# Getting user input.
# Storing input in list with removing duplicates.
while word!='':
    if word not in words:
        words.append(word)
    word = input('> ')

# Output list contain inputs with no duplicates.
print(words)
'''

foo = []
foo.insert(0,'alfa')
print(foo)
























