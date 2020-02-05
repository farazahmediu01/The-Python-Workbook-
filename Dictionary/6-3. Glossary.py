favorite_words = {
    'poll': 'similar values',
    'get': 'method to avoide key error',
    'item()': 'it is a method for looping key-value pair',
    'phytamine': 'drug',
    'bool': 'true or false',
}
keys = ['aslam', 'iqbal', 'monalisa', 'babar']
values = ['bhai', 'taurey', 'drift queen', 'dhatoora']

print("len =",len(favorite_words))

for key, value in zip(keys, values):
    favorite_words[key] = value

for key, value in favorite_words.items():
    message = f"\n{key}:\n{value.title()}"
    print(message)
print('len =',len(favorite_words))