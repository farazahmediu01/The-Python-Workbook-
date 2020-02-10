sports = ['hockey', 'football']

inp = input('Enter your favorite sports: ')
sports.append(inp)

print("List of sports is shown blow")
for item in sorted(sports):
    print(item.title())