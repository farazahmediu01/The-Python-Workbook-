TV_CHENNALS = ['sama news', 'geo news', 'aaj news', 'ary news']
validation = "y"

def insert_new_chennal(name, index):
    index = index - 1
    TV_CHENNALS.insert(index,name)

def show_chennal():
    for chennal in TV_CHENNALS:
        print(chennal.title())


while validation.lower() == "y":
    show_chennal()
    message = f"Enter number between 1 to {len(TV_CHENNALS)}: "

    print("\nEnter name of Tv chennal you want to enter in your chennal list.")
    name = input(">")

    # Contineu from here skip all line above,?
    # I think i can be done with some if contions
    # or with a while loop but you tell me any think
    # convinent
    print(f"\nSet number to {name.title()} chennal.")
    index = input(message)
    try:
        index = int(index)
    except:
        print("\nError")
        print("Enter number please.")
        continue

    insert_new_chennal(name,index)
    print("\nDo you want to add more chennals?")

    

    validation = input("Press [y/n]: ")
