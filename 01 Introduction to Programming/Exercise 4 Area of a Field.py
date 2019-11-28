print("\n\nProgram start from here...\n")

# User input for lenght and weight.
user_l = float(input("Enter length in feet: "))
user_w = float(input("Enter width in feet: "))

# Formula.
aera_of_field          = user_l * user_w
area_of_field_in_acers = aera_of_field / 43560

# Output.
print("The area of field in acre is", area_of_field_in_acers, "square feet.")
