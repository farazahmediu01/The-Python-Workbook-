def popup_item(n, series):
    deleted_items = []
    item_1 = None
    item_2 = None

    for i in range(n):
        item_1 = series.pop()
        item_2 = series.pop(0)

        deleted_items.extend([item_1, item_2])
    return sorted(deleted_items)


def remove_outliers(n, series=None):
    '''n is the amount of extereme values
    to be remove from starting and ending
    of a given list which is the second parameter'''

    if n < 0:
        print("Error\nFirst parameter should be a positive integer.")
    elif len(series) <= 4:
        print("Error\nSecond parameter must conatin more than 4 elements.")

    series = series[:]
    series.sort()
    deleted_items = popup_item(n, series)

    return series, deleted_items


series = []
number_of_outliers_to_delete = None
inp = None

print("Enter numbers or press enter to skip")
while inp != '':

    inp = input(">")
    try:
        inp = int(inp)
    except:
        continue

    series.append(inp)

print("\nHow many outliers you want to delete")
inp = int(input("Enter number only: "))
new_serires, outliers = remove_outliers(inp, series)

print("\nOriginal List", sorted(series))
print("List without outliers", new_serires)
print("Deleted Outliers", outliers)
