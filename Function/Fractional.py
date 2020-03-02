def fractional_part(numerator, denominator):
    if denominator == 0: return 0
    
    division = numerator / denominator
    only_fraction = division - int(division)
   
    return only_fraction


result = fractional_part(5, 4)
print(result)

