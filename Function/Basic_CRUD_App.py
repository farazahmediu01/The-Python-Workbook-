# Create Read Update Delete (CRUD)


def add(user_input, array):
    '''This function insert an element into a list as a new slot.'''
    return array.append(user_input)


def read():
    return sorted(array)


def delete(user_input, array):
    index = array.index(user_input)
    del array[index]

def input_loop(number=5):
    '''Main input loop'''
    user_input = None
    count = 0

    while (count <= number) and (user_input != ""):
        user_input = input(">")
        #create(user_input, array)
        
        
        count += 1
    


def main():
    # Initialzing variables.
    message = "Enter five names of your friends "
    message += "you want to invite in your party."
    message += "\n(press enter to skip)."
    array = list()
    #count = 0
    #user_input = None
    print(message)
    
    input_loop()


    # Main loop.
    
