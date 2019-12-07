def sort_integers(a,b,c):
    smallest = min(a,b,c)
    largest = max(a,b,c)
    middle = (a + b + c) - (smallest  + largest)
    
    return smallest, middle, largest

print(sort_integers(22, 14, 11))