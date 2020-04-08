
def press_validation(press):    # Check
    # This block verify that user input must be a number 'a' 'd' and 'r'.
    # User can only 'Add' 'Delete' and 'Read' data if this fuction returns True.
    if press == 'a' or press == 'd' or press == 'r' or press == 'e':
        return True
    else:
        return False


def input_loop():   # Check
    '''This function starts a loop of user input until user enter an empty string.
    each input will stored in a list of all inputs, it returns 'input_list' '''

    inp = None
    inp_list = list()
    print(f"\nEnter names, (press enter to skip).")

    while inp != "":
        inp = input(">")
        if inp:
            inp_list.append(inp)

    return inp_list


def delete_names(names_to_delete, names):   # Check
    '''This fuction get a list of names and delete
    all names from the original list and return back
    the deleted names'''

    deleted_names = []

    for x in names:
        if x in names_to_delete:
            while x in names:
                index = names.index(x)
                item = names.pop(index)
                deleted_names.append(item)
    
    return deleted_names


def sorted_names(inp, names_to_sort):
    '''This function print names in a sorted form if user ented yes otherwise names printed as they were sorted.'''
    print()
    if inp.lower() == 'y':
        for name in sorted(names_to_sort):
            print(name.title())
    else:
        for name in names_to_sort:
            print(name)


def number_validation(number, message):
    # This block is skip due to complexity and non user friendly key mappings.
    # This function is used in the '1' and '2' part where the user enter number for add or delete names.
    if number.isnumeric():
        return int(number)
    else:
        print(f"\nYou are trying to '{message.title()}' names.")
        print(
            f"Enter a number so that system can determine how many names you want to {message}.")
        while True:
            print("\nEnter number only.")
            number = input(">")
            try:
                return int(number)
            except:
                continue

def make_file(names):
    with open('file.txt', 'a') as file_handle:
        for name in names:
            file_handle.write(f"\n{name}")

            