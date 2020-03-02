even_numbers = []
odd_numbers = []
message = "\nEnter a number so till that number "
message += "we give a list of even and odd seperately: "


def even(number):
    if number % 2 == 0:
        return True

    return False


def main():
    print(message)
    user_input = int(input(">"))

    for i in range(1, user_input + 1):
        if even(i):
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    print("Odd  =", odd_numbers)
    print("Even =", even_numbers)


if __name__ == "__main__":
    main()
