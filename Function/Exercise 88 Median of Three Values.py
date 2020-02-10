print("\nThis program tells you the median of 3 numbers, please enter three numbers.")


def cal_median(a, b, c):
    if a > b and a < c or a < b and a > c:
        return a
    elif b > a and b < c or b < a and b > c:
        return b
    elif c > a and c < b or c < a and c > b:
        return c

def alternate_median(a, b, c):
    return (a + b + c) - (min(a, b, c) + max(a, b, c))

def main():
    while True:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))        
        median = cal_median(a, b, c)
        alt_median = alternate_median(a, b, c)        
        print(f"{'_' * 20}\nMedian = {median:.2f}\nMedian using alternative method {alt_median}\n{'_' * 20}")


main()
