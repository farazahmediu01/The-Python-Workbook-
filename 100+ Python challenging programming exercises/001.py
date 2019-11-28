
'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
a = None

print("\n\nFirst program\n\n")
p = []

for i in range(2000,3201):
    if (i%5 != 0) and (i%7 == 0):
        p.append(str(i)) # print(i,end=",")
a = ','.join(p)

#print(j)
print("a =",len(a))

a = None

print("\nSecond Program\n")

for i in range(2000,3201):
    if (i%5 != 0 ) and (i%7 == 0):                   
        print(i,end=",")

#print(len(print(i,end=",")))












