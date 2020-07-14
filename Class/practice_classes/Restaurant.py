class Restaurant:
    """This Class defines a Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """This Class has tow attributes resturant_name and cusion type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name}!")

    def open_restaurent(self):
        print(f"{self.restaurant_name} is open!")


restuarant_1 = Restaurant("Javaid Nihari", "Desi Food")
restuarant_2 = Restaurant("Ideal 36", "Ice-cream paular")

restuarant_1.describe_restaurant()
restuarant_2.describe_restaurant()

restuarant_1.open_restaurent()
restuarant_2.open_restaurent()


