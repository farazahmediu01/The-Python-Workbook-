inp = None
neg_list = []
pos_list = []
zeros_list = []
final_list = []

while inp != '':
    inp = input("Enter number: ")

    try:
        inp = int(inp)
    except:
        print("Error.")
        print("Enter number only.")
        continue

    if inp > 0:
        pos_list.append(inp)
    elif inp < 0:
        neg_list.append(inp)
    elif inp == 0:
        zeros_list.append(inp)

final_list.extend(neg_list)
final_list.extend(zeros_list)
final_list.extend(pos_list)

print(final_list)
