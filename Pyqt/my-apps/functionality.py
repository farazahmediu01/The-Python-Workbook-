
def press_validation(press):
    # This block verify that user input must be a number 'a' 'd' and 'r'.
    # User can only 'Add' 'Delete' and 'Read' data if this fuction returns True.
    if press == 'a' or press == 'd' or press == 'r' or press == 'e':
        return True
    else:
        return False


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


def input_loop():
    # This funtion start a loop for user input the range is defined by user and loops ends with an empty string.
    #count = 0
    inp = None
    input_array.clear()
    #print(f"\nEnter {number} names, (press enter to skip).")
    print(f"\nEnter names, (press enter to skip).")

    while inp != "":  # (count < number) and (inp != ""):
        inp = input(">")
        if inp:
            input_array.append(inp)
        # count += 1
    return input_array


def delete_names(names):
    # Error
    for x in names:
        while x in storage:
            storage.remove(x)


def sorted_names(n):

    # This function print names in a sorted form if user ented yes otherwise names printed as they were sorted.
    print()
    if n.lower() == 'y':
        for name in sorted(storage):
            print(name.title())
    else:
        for name in storage:
            print(name)
