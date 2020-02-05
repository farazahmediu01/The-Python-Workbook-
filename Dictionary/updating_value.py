faraz = {'name': 'faraz', 'age': '22', 'cell': 'mobile'}
print(faraz)
dot = '.'

for key in faraz:
    '''faraz[key] = faraz[key] + dot * 3'''
    key = key + dot * 3
    print(key)

print(faraz)
