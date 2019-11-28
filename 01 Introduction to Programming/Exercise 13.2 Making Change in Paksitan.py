print("\n\nProgram start now...\n")
# This proram is for making change.

# Setting variables, all possible amount of change.
one_rup             = 1
two_rup             = 2
five_rup            = 5
ten_rup             = 10
twenty_rup          = 20
fifty_rup           = 50
hundred_rup         = 100
five_hundered_rup   = 500
thousand_rup        = 1000

# While loop is also called infinite loop because it have no limit of itration. 
# 
while True:
    # User input or the amount which have been entered for making change.
    rupees = input("\nEnter amount in Rupees: ")
    print()
    
    if rupees == 'quit':
        break

    try:
        rupees = int(rupees)
    except:
        print("Enter numbers only")
        print("if you want to Exit type 'quit'. ")
        continue
    
    # Output of the program.
    if rupees // thousand_rup != 0 :
        print("Thousand Rupees     =",            (rupees // thousand_rup))
    rupees = rupees % thousand_rup

    if rupees // five_hundered_rup != 0 :
        print("Five Hundred Rupees =",            (rupees // five_hundered_rup))
    rupees = rupees % five_hundered_rup

    if rupees // hundred_rup != 0 :
        print("Hundred Rupees      =",            (rupees // hundred_rup))
    rupees = rupees % hundred_rup

    if rupees // fifty_rup != 0 :
        print("Fifty Ruppes        =",            (rupees // fifty_rup))
    rupees = rupees % fifty_rup

    if rupees // twenty_rup != 0 :
        print("Twenty Rupees       =",            (rupees // twenty_rup))
    rupees = rupees % twenty_rup

    if rupees // ten_rup != 0 :
        print("Ten Rupees          =",            (rupees // ten_rup))
    rupees = rupees % ten_rup

    if rupees // five_rup != 0 :
        print("Five Ruppes         =",            (rupees // five_rup))
    rupees = rupees % five_rup

    if rupees // two_rup != 0 :
        print("Two Rupees          =",            (rupees // two_rup))
    rupees = rupees % two_rup

    if rupees // one_rup != 0 :
        print("One Ruppes          =",            (rupees // one_rup))
    rupees = rupees % one_rup
    
    print("."*30)