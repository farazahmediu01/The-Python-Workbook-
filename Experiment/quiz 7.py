# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the min_01 and max_02 of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and 
# put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.
min_01  = None
max_02 = None

while True:
    num = input("Enter integer: ")
    
    if num == 'done':
        break
   
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    
    #sm = sm + line 
    
    if min_01 is None :
        min_01 = num
    
    if max_02 is None : 
        max_02 = num
    
    if num < min_01 :
        min_01 = num
    
    elif num > max_02 :
        max_02 = num
    
    

print("Maximum =",max_02)
print("Minimum =",min_01)