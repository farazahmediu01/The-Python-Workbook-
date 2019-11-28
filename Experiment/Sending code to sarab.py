print("\n\nProgram start now...\n")

#
# Read it carefully.
# This proram is for making change for the currency of Pakistan.
# If you give the amount in Ruppes, this program will give you back
# the minimun amount of Notes or Coins which are equivalent to the amount you have entered.
#


# Setting up variables, all possible amount of change.

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
# So for this we have a "break" statement to stop the loop.
# We set this break keyword with "quit" command, you will see below.


while True:
    
    
    # User enter the amount for making change.
    
    rupees = input("\nEnter amount in Rupees: ")  # User input stored in a variable we named as ruppes. 
    print()                                       # This print statement is inly for line break. 
    
    if rupees == 'quit':                          # This is the triger to stop the loop with "quit".
        break

    
    # Try and Except are for catching errors.
    # Try try to convert the string into integer.
    # If Try fails to convert the string into integer the except part will executes safly, with an error massage
    
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