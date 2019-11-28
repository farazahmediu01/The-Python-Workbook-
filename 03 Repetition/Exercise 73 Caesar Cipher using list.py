'''
8)print(fruit_list.index("apple")) 
# This function tells you what is the "index number" of "apple" in fruits_list.

3)num_list.insert(0,6)    
# This function countains two parameter first is "index number" which is "zero" and the second parameter is the value to be inserted which is "six".

'''








text                = input("Enter text: ")
text_list           = []
alphabets           = "abcdefghijklmnopqrstuvwxyz"
alphabets_list      = []
incripted_list      = []

for a in alphabets:             # generating alphabets list
    alphabets_list.append(a)

for b in text:                   # generating text list
    text_list.append(b) 

for each_value in text_list:           
    if each_value in alphabets_list:
        alphabets_list.index(each_value)    # the index number of element in alphabet list.       # i need a function which tells the index of list element
        


    