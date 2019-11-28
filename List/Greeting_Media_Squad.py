media_squad = ['faraz', 'sameer', 'sarab', 'ali']
name = input('Enter your name or your squad name: ')
print()

if name in media_squad:
    
    if name == media_squad[0]:
        print(f'Hello {media_squad[0].title()}, how are you?')
    
    elif name == media_squad[1]:
        print(f'Hello {media_squad[1].title()}, how are you?')
    
    elif name == media_squad[2]:
        print(f'Hello {media_squad[2].title()}, how are you?')

    elif name == media_squad[3]:
        print(f'Hello {media_squad[3].title()}, how are you?')
