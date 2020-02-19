prompt = "\nTell me anything i will repeat it."
prompt += "\nPress Enter to quit. "
active = True

while active:
    user_input = input(prompt)
    
    if user_input == '':
        active = False 
    else:
        print(user_input.title())