array = list(range(1,11))     # An array from 1-10.
array.reverse()
temp  = 0
index = 0                     # temp variable helps in swaping values of list elements.
print("list =",array)         # printing list before changing it.

for i in range(1,6):               # (loop) to make change in every element
    
    if array[i] < array[index]:     # (condition) to ensure what to change, we are looking for a big value to swap with the position of small value, so we have to track both index and value 
                                    # [10,9,8,7,6,5]
                                    # [9,10,8,7,6,5]
                                    # []
                                    # [5,6,7,8,9,10] 
        
        temp = array[index]         # using temp to store list element.
        array[index] = array[i]     # swaping 
        array[i] = temp
        index = i
        break 

print("list =",array) 




'''
array[0] = array[4]
array[4] = 0

print("list =",array)
'''

