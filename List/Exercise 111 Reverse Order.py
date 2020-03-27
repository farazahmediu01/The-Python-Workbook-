series = []
inp = None

while inp != '':
    if inp == None:
        inp = input("Enter number: ")
    series.append(int(inp))
    inp = input('Enter number: ')

series.sort(reverse=True)
print(series)
