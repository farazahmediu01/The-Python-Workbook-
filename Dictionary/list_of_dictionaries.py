faraz = {'name': 'faraz ahmed', 'age': 22, 'home': 'dastagir'}
sameer = {'name': 'sameed ahmed', 'age': 22, 'home': 'hina homes'}
sarab = {'name': 'sarab ali khan', 'age': 21, 'home': 'disko' }
ali = {'name': 'mohammad ali khan', 'age': 23, 'home': 'johor'}
media_squad = [faraz,sameer,sarab,ali]

for item in media_squad:
    #for key in item:
        #if key == 'age':
            #print(key)
    item['age'] = 0

for item in media_squad:
    print(item)
