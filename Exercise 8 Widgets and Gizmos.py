print("\n\nProgram start now...\n")
# This program calculate the weight of given two products Wedgit and Gizmos.

# User input number of products.
product_1 = int(input("Enter number of Wedgit: ")) 
profuct_2 = int(input("Enter number of Gizmos: "))

# Each widget weighs 75 grams. Each gizmo weighs 112 grams.
formula = (product_1 * 75) + (profuct_2 * 112)

# Output shown below.
print("\nThe total weight of %d wegets and %d gizmos is %.2f gram." %(product_1, profuct_2,formula))
