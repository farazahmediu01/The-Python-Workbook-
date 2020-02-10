countries = ('pakistan', 'australia', 'india', 'china', 'germany')

for index in range(len(countries)):
    print(countries[index].title())

inp = input('Enter the country name you like: ')
print(f"\nThe country {inp.title()} is number {countries.index(inp.lower()) + 1} on the list.")

inp = int(input('Enter number: '))
print(f"The country {countries[inp]} is {inp} in the list.")
