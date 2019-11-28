def even_parity_bit(data):
    return len(data)%8 == 0

data = input(">")
while data != "":     
    print("The bits transmitted in set of 8 pairs?",even_parity_bit(data))
    data = input(">")

