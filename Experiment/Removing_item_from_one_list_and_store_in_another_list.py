a     = []
b     = []
index = 0

# adding number from 0 to 10 in list a.

for i in range(11):
    a.append(i)
print("a =",a)

#adding numbers in b from the end of list a and at the same point also removing the number from a.

for i in range(a.index(10) + 1):
    b.insert(index,a.pop())
    index += 1

print("b =",b)
print("\na =",a)
print("b =",b)