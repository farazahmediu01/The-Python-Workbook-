def valid_name():
    print("The name should consist on between 3 to 7 charachters.")
    name = input("Enter name: ")

    if len(name) >= 3 and len(name) <= 7:
        return True

    return False


def verify_valid_name():
    while not valid_name():
        valid_name()
    print("Done")
    
verify_valid_name()
