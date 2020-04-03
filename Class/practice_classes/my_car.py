class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        description = f"{self.year} {self.make} {self.model}"
        return description

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You cannot roll back odometer!")

    def increment_odometer(self, miles):
        miles += self.odometer_reading
        self.update_odometer(miles)
    
    def full_gas_tank(self):
        print(f"The gas tank of {self.get_description()} is full now!")
    
     
car_1 = Car('Honda', 'City', '2019')
car_2 = Car('Toyota', 'Land Cruiser', '1982')


