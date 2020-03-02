divisor = None

def prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            divisor = i
            return False

    return True


def main():
    inp = None
    while inp != '':

        inp = input("\nEnter number, (press enter to skip): ")
        
        try:
            inp = int(inp)
        except:
            if inp == '':
                continue
            else:
                print("Enter numbers only.")
                continue
        

        if prime(inp):
            print(f"Yes, {inp} is a prime number.")
        else:
            print(f"No, {inp} is not a prime number.")
            #print(f"Because it is evenly divided by {divisor}")

        #print(inp,"is a prime number." if prime(inp) else "is not a prime number.")
        #inp = input("\nEnter number: ")


if __name__ == "__main__":
    main()
