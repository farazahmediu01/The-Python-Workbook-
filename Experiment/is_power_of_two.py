def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    if n != 0:
        while n % 2 == 0:
            n = n / 2

    # If after dividing by two the number is 1, it's a power of two
    if n == 1:  # 0
        return True
    return False


'''
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False
'''


def multiplication_table(start, stop):
    for x in range(start, stop):
        for y in range(x, stop):
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
