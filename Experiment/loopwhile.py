smalles_number = 0
lis = [100 , 1, 2, 3, 4, 5 , 100 ]
print("Before",smalles_number)
for i in lis :
    if i == lis[0]:
        smalles_number += i
    if i < smalles_number :
        smalles_number = i
    print("small =",smalles_number,"i =",i)
print("After",smalles_number)
