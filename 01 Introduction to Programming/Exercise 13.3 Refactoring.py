# Variable 'notes' contain all possible Banknotes and coins in Pakistani currency.
notes = (1000, 500, 100, 50, 20, 10, 5, 2, 1)

# make_change contain the logic part.
def make_change(rupees):
    for note in notes:
        if rupees // note != 0:
            print(f"{note}\t=\t{(rupees // note)}")
        rupees = rupees % note


while True:
    rupees = input("\nEnter amount in Rupees: ")
    print()
    if rupees.lower() == 'e':
        break
    try:
        rupees = int(rupees)
    except:
        print("Enter numbers only")
        print("Press 'e' to Exit. ")
        continue
    make_change(rupees)
    print()
