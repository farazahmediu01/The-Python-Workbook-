def sort_integers(a,b,c):
    smallest = min(a,b,c)
    largest = max(a,b,c)
    middle = (a + b + c) - (smallest  + largest)
    
    return smallest, middle, largest

x = []

while len(x) < 3:
    i = int(input("Enter value: "))
    x.append(i)

a,b,c = x
print(sort_integers(a,b,c))
