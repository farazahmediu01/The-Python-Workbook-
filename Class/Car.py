class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        description = f"{self.year} {self.make} {self.model}"
        return description.title()
    
    def read_odometer(self):
        reading = f"This car has {self.odometer_reading} miles on it."
        print(reading)
    
    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


car_1 = Car("Honda", "Civic", 2019)
car_2 = Car("Toyota", "Corrolla", 2018)

# # print(car_1.get_description())
# # print(car_2.get_description())
# # car_1.make = 'suzuki'

# # print(car_1.get_description())
# car_1.update_odometer(2)
# car_1.read_odometer()
# car_1.increment_odometer(-1)
# car_1.read_odometer()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def get_battery_discription(self):
        discription = f"This car has a battery of {self.battery_size} KWH."
        return discription

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_description())
my_tesla.update_odometer(55)
my_tesla.increment_odometer(4)
my_tesla.read_odometer()
print(my_tesla.get_battery_discription())

# print(my_tesla.get_battery_discription().lower().split('a'))