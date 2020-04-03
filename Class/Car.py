class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        description = f"{self.year} {self.make} {self.model}"
        return description.title()

    def fill_gas_tank(self):
        print(f"Gas tank of {self.get_description()} is filled.")

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


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def set_battery_size(self, size):
        self.battery_size = size

    def get_battery_description(self):
        discription = f"This car has a battery of {self.battery_size} KWH."
        return discription


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"The car {self.get_description()} has no fule tank.")





# Rough work.

# car_1 = Car("Honda", "Civic", 2019)
# car_2 = Car("Toyota", "Corrolla", 2018)

# # print(car_1.get_description())
# # print(car_2.get_description())
# # car_1.make = 'suzuki'

# # print(car_1.get_description())
# car_1.update_odometer(2)
# car_1.read_odometer()
# car_1.increment_odometer(-1)
# car_1.read_odometer()
# car_1.fill_gas_tank()
# my_tesla = ElectricCar('tesla', 'model s', '2019')
# print(my_tesla.get_description())
# my_tesla.update_odometer(55)
# my_tesla.increment_odometer(4)
# # my_tesla.read_odometer()
# print(my_tesla.get_battery_description())
# my_tesla.fill_gas_tank()
# print(my_tesla.get_battery_discription().lower().split('a'))
# Car.odometer_reading = 96

# car_1.update_odometer(5)
# car_2.update_odometer(10)
# my_tesla.update_odometer(15)


# print(car_1.odometer_reading)
# print(car_2.odometer_reading)
# print(my_tesla.odometer_reading)

# car_1.wheels = 19

# print(car_1.wheels)
# print(car_2.wheels)
# print(my_tesla.wheels)

tesla_1 = ElectricCar('tesla', 'model pd 100', 2020)
tesla_2 = ElectricCar('tesla', 'model s', 2019)

tesla_1.battery.battery_size=2000
# print(tesla_1.battery.get_battery_description())