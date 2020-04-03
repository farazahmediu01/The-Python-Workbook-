class Battery:
    def __init__(self, battery_size=100):
        self.battery_size = battery_size
    
    def read_battery(self):
        print(f"The size of this battery is {} ")

    def update_battary(self, battery_size):
        self.battery_size = battery_size
    
    def show_battary_power(self):
        if self.battery_size <= 100:
            print("This car can travel upto 100 Miles.")
        elif 100 < self.battery_size <= 200:
            print("This car can travel upto 200 Miles.")
        elif 300 < self.battery_size <= 400:
            print("This car can travel upto 300 Miles.")
            

power_plus = Battery()
exel = Battery()

print(power_plus)