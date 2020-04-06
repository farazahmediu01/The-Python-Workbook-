class Car:
    '''This Car class define a car'''

    def __init__(self, make, model, year):
        '''This init method contains 3 positonal attributes
        and one default attribute'''
        self.make = make
        self.model = model
        self.year = year
        # This attribute set by default to all instances.
        self.odometer_reading = 0

    def get_description(self):
        '''Return descriprive name'''
        description = f"{self.year} {self.make} {self.model}"
        return description

    def read_odometer(self):
        '''print odometer reading'''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        '''Update odometer'''
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You cannot roll back odometer!")

    def increment_odometer(self, miles):
        '''Increament odometer'''
        miles += self.odometer_reading
        self.update_odometer(miles)

    def full_gas_tank(self):
        '''Print a line telling gas tank description 
        od perticulat car-'''
        print(f"The gas tank of {self.get_description()} is full now!")



'''
car_1 = Car('Honda', 'City', '2019')
car_2 = Car('Toyota', 'Land Cruiser', '1982')

my_tesla = ElectricCar('Tesla', 'Roadster', 2020)
my_tesla.full_gas_tank()
'''