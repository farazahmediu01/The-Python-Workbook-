class Restaurant:
    '''This is a Restaurant class.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initially there are only two attriutes 
        restaurant_name and cuisine_type.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''This method describe two attributes of an instance.'''
        describe_text = f"{self.restaurant_name} {self.cuisine_type}"
        return describe_text.title()

    def open_restaurent(self):
        '''This method tells the restaurant is open.'''
        open_message = f"The {self.restaurant_name.title()} is open!"
        return open_message

    def print_info(self):
        '''This function print the information return by 
        describe_restaurant and open_restaurent so you don't have to.'''
        information = f"{self.describe_restaurant()}\n{self.open_restaurent()}\n"
        print(information)


restaurant_1 = Restaurant('makrani hotel', 'desi dhaba')
restaurant_2 = Restaurant('ghreeb nawaz hotel', 'desi tarka')
restaurant_3 = Restaurant('dhaba spice', 'fast food')
restaurant_4 = Restaurant('javaid nihari', 'triditional desi food')

restaurant_1.print_info()
restaurant_2.print_info()
restaurant_3.print_info()
restaurant_4.print_info()
