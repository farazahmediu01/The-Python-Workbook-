class Restaurant:
    '''This is a Restaurant class.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initially there are only two attriutes 
        restaurant_name and cuisine_type.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''This method describe two attributes of an instance.'''
        describe_text = f"{self.restaurant_name.title()} is a {self.cuisine_type.title()} shop."
        return describe_text

    def open_restaurent(self):
        '''This method tells the restaurant is open.'''
        open_message = f"The {self.restaurant_name.title()} is open!"
        return open_message

    def print_info(self):
        '''This function print the information return by 
        describe_restaurant and open_restaurent so you don't have to.'''
        information = f"\n{self.describe_restaurant()}\n{self.open_restaurent()}"
        information += f"\nNumber served = {self.number_served}"
        print(information)

    def set_number_served(self, number):
        '''This method is set value for attribute number_served 
        only if the value is grater then or equal to the privious value.'''
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You cannot roll back the value of number severd.")

    def increment_number_served(self, increment):
        '''It increments the value of attribute number_served.'''
        # if increment >= self.number_served:
        # self.number_served += increment
        increment = self.number_served + increment
        self.set_number_served(increment)


class IceCreamStand(Restaurant):
    '''This class is inheret from Restuarant.
    it a practice from book Python crash course
    by eric methews, chapter 9-6 Ice Cream Stand.'''

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"\nFollowing are the flowers in {self.restaurant_name.title()}:")
        for count, flavor in zip(range(1, len(self.flavors) + 1), self.flavors):
            message = f"{count}) {flavor.title()}"
            print(message)
    def print_flavor_list(self):
        print(self.flavors)

ice_shop_1 = IceCreamStand('ideal 36','ice cream','vanila', 'chocolate', 'blue_berry', 'cheeku', 'kaju', 'kulfa')
ice_shop_2 = IceCreamStand('creamy', 'ice cream','chocolate chip', 'blue berry', 'pista', 'peanut', 'kit-kat', 'dairy-milk', 'pishawri')

print(ice_shop_1.describe_restaurant())
print(ice_shop_2.describe_restaurant())

ice_shop_1.display_flavors()
ice_shop_2.display_flavors()

ice_shop_1.print_flavor_list()
ice_shop_2.print_flavor_list()



'''
restaurant_1 = Restaurant('makrani hotel', 'desi dhaba')
restaurant_2 = Restaurant('ghreeb nawaz hotel', 'desi tarka')
restaurant_3 = Restaurant('dhaba spice', 'fast food')
restaurant_4 = Restaurant('javaid nihari', 'triditional desi food')

print()
restaurant_1.print_info()
restaurant_1.set_number_served(12)
print("set_num =",restaurant_1.number_served)
restaurant_1.increment_number_served(3)
print("increment number 3, 12 + 3 = " + str(restaurant_1.number_served))


# print()
restaurant_2.print_info()
restaurant_2.set_number_served(6)
print("set num 6 : ",restaurant_2.number_served)
print('show roll back error')
restaurant_2.set_number_served(5)
restaurant_2.increment_number_served(4)
print("increment 4, 6+4 10: ",restaurant_2.number_served)


# print()
restaurant_3.print_info()
restaurant_3.increment_number_served(10)
print('derect increment 10:',restaurant_3.number_served)


# print()
restaurant_4.print_info()
restaurant_4.increment_number_served(5)
print("direct increament 5:", restaurant_4.number_served)
print("error roll back")
restaurant_4.set_number_served(4)

restaurant_4.set_number_served(6)
print("set 6:", restaurant_4.number_served)
'''
