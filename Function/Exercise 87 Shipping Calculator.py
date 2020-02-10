FIRST_ITEM_RATE = 10.95
SUBSEQUENT_ITEM_RATE = 2.95

def cal_shipping_charge(items):
    if items == 1:
        return FIRST_ITEM_RATE
    elif items > 1:
        return (items - 1) * SUBSEQUENT_ITEM_RATE + FIRST_ITEM_RATE
    
def main():
    print("\nThis program tells you the shipping price of emtered items with repect to the defined rates.")
    items = int(input("Enter the number of items: "))
    shipping_charge = cal_shipping_charge(items)
    print(f"The shipping rate of {items} items is ${shipping_charge:.2f}")

main()