POSSIBLITY_PER_LETTER = 26
#user_inp = int(input("Enter number: "))
PASSWORD_LENGHT = 6
TOTAL_POSSIBLITIES = POSSIBLITY_PER_LETTER ** PASSWORD_LENGHT
message = f"\nThe total possiblities in a {PASSWORD_LENGHT} charachter string is equal to {TOTAL_POSSIBLITIES}"

print(message)
