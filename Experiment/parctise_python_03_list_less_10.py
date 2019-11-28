inp = int(input(">"))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < inp:
        b.append(i)
print(b)   