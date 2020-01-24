def maximum_number(first, second, third):
    maximum = 0

    maximum = first: if (first > second) and (first > third)
    maximum = second elif (second > first) and (second > third)
    maximum = third elif (third > first) and (third > second)

    return maximum


get_value_1 = maximum_number(-19, 33, -37)
get_value_2 = maximum_number(122, 12, 144)
get_value_3 = maximum_number(-100, -23, -243)

print(get_value_1)
print(get_value_2)
print(get_value_3)
