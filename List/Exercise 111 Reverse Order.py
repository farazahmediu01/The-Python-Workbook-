series = []
inp = 0

while inp != '':    
    series.append(int(inp))
    inp = input('Enter number: ')

series.sort(reverse=True)
print(series[:-1])

