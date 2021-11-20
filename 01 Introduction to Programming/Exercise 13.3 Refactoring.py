# Variable 'notes' contain all possible Banknotes and coins in Pakistani currency.
notes = (1000, 500, 100, 50, 20, 10, 5, 2, 1)

# make_change contain the logic part.
def make_change(rupees):
    for note in notes:
        if rupees // note != 0:
            print(f"{note}\t=\t{(rupees // note)}")
        rupees = rupees % note

print("Progarm starts press 'e' to exit.")
while True:
    rupees = input("\nEnter amount in Rupees: ")
    if rupees.lower() == 'e':
        break
    try:
        rupees = int(rupees)
    except:
        print("\nEnter numbers only")
        print("\nPress 'e' to Exit. ")
        continue
    make_change(rupees)
    print()
