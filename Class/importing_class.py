from car import Car


car1 = Car('suzuki', 'margala', '1982')
print(car1.get_description())

car1.update_odometer(12)
car1.increment_odometer(4)
car1.read_odometer()