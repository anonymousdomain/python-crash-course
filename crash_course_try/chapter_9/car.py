class Car:
    def __init__(self, make, model, year):
        self.manfacturer = make
        self.model = model
        self.year = year
        self.odometer_reading = 63  # setting a default value for attribute

    def describe_car(self):
        full_name = f"{self.manfacturer} {self.model} {self.year}"
        return full_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")

    def update_odometer(self, milege):
        """ upditaing the reading"""
        if milege >= self.odometer_reading:
            self.odometer_reading = milege
        else:
            print(f"you cant roll back the odometere")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battry:
    def __init__(self, battry_size=75):
        self.battry_size = battry_size

    def describe_battry(self):
        if self.battry_size == 75:
            print(f"this car has {self.battry_size}kwh in a full charge")
        elif self.battry_size == 100:
            print(f"this car battry has been upgraded to {self.battry_size}")

    def get_range(self):

        if self.battry_size == 75:
            mile = 275
        elif self.battry_size == 100:
            mile = 350

        print(f"this car can go about {mile} miles on a full charge")

    def upgrade_battry(self):
        self.battry_size = 100
        # print(f"batrry size upgraded to {self.battry_size}kwh")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battry = Battry()

