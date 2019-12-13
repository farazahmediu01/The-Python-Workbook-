def sort_integers(a,b,c):
    smallest = min(a,b,c)
    largest = max(a,b,c)
    middle = (a + b + c) - (largest + smallest)
    
    return smallest, middle, largest

x = []

while len(x) < 3:
    i = float(input("Enter value: "))
    x.append(i)

a,b,c = x[0], x[1], x[2]
print(sort_integers(a,b,c))
