class Car:
    """This Class define a car"""

    def __init__(self, make, name, model):
        self.make = make
        self.name = name
        self.model = model

    def describe_car(self):
        print(f"{self.model} {self.makegit} {self.name}")


car_1 = Car("Honda", "BRV", "2015")
car_2 = Car("Suzuki", "Cultus", "2004")
car_3 = Car("Toyota", "Corrola", "2016" )

car_1.describe_car()
car_2.describe_car()
car_3.describe_car()
