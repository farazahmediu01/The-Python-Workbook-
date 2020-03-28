class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"


car_1 = Car("Honda", "Civic", 2019)
car_2 = Car("Toyota", "Corrolla", 2018)

print(car_1.description())
print(car_2.description())
