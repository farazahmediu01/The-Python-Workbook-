def get_largest(data, box=None):
    for x in data:
        if box == None:
            box = x
        elif box < x:
            box = x
    return box


data = [7, 24, 62, 11, 444, 39, 42, 5, 97, 54, 0, 102]
print(get_largest(data))
