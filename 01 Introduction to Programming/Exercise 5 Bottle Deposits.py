print("\n\nProgram start from here...\n")

# Given deposite.
deposite_low  = 0.10
deposite_high = 0.25

# User input number of small and big container.
user_small_cont    = int(input("Enter number of drink containers holding one liter or less: "))
user_big_cont      = int(input("Enter number of drink containers holding more than one liter: "))

# Formula.
refund_low  = user_small_cont * deposite_low
refund_high = user_big_cont * deposite_high

# Output.
print("\nCongratulation you received refund of $%.2f on small container."   %(refund_low))
print("Congratulation you received refund of $%.2f on big container."       %(refund_high))
print("\nTotal refund is $%.2f."                                            %(refund_low + refund_high))


