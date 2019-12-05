array = list(range(1,11))     # An array from 1-10.
array.reverse()
temp = 0
index = 0                     # temp variable helps in swaping values of list elements.
print("list =",array)         # printing list before changing it.

for i in range(1,11):               # (loop) to make change in every element
    if array[i] > array[index]:     # (condition) to ensure what to change, we are looking for a big value to swap with the position of small value, so we have to track both index and value 
        
       
        temp = array[index]
        array[index] = array[i]
        array[i] = temp
        index = i 

print("list =",array) 




'''
array[0] = array[4]
array[4] = 0

print("list =",array)
'''

