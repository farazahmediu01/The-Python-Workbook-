def make_box(symbol, width, lenght):
    space = ' ' * len(symbol)
    print(symbol * width)

    for i in range(height):
        print(f"{symbol}{(width - 2) * space}{symbol}")

    print(symbol * width)


print("Enter the following inputs to print a box.")
symbol = input("Enter symbol: ")
width = int(input("Enter width: "))
height = int(input("Enter height: "))

make_box(symbol, width, height)
