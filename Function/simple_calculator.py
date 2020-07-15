def add(int_1, int_2):
    return int_1 + int_2


def sub(int_1, int_2):
    return int_1 - int_2


def mul(int_1, int_2):
    return int_1 * int_2


def div(int_1, int_2):
    return int_1 / int_2


def main():
    int_1 = float(input("Enter 1st number: "))
    int_2 = float(input("Enter 2st number: "))
    print("Enter 1 to add, 2 to subtract , 3 to multiple and 4 to divide")
    operator = int(input(">"))

    if operator == 1:
        result = add(int_1, int_2)

    elif operator == 2:
        result = sub(int_1, int_2)

    elif operator == 3:
        result = mul(int_1, int_2)

    elif operator == 4:
        result = div(int_1, int_2)

    print(result)


if __name__ == '__main__':
    main()
