def greet_user(name):    
    message = f'Hello {name.title()}, How are you!'
    return message

name = input('Enter name: ')
a = greet_user(name)
print(a)