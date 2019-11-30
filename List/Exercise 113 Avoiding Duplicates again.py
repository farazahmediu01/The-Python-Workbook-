words = []

print('\nEnter a word (blank to quit):')
word = input('> ')

while word!='':
    if word not in words:
        words.append(word)
    word = input('> ')

print(words)
        


