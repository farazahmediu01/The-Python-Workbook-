def maximum_number(first,second,third):
    maximum = 0
    
    if first    > (second and third):    maximum = first
    elif second > (first and third):     maximum = second
    elif third  > (first and second):    maximum = third
    
    return maximum

get_value_1 = maximum_number(19, 33, 37) 
get_value_2 = maximum_number(122, 112, 144)
get_value_3 = maximum_number(-100, -23, -243)

print(get_value_1)
print(get_value_2)
print(get_value_3)    

