class Car :
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year) :
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) :
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self) :
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage) :
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else :
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles) :
        self.odometer_reading += miles

    def fill_gas_tank(self) :
        print("This car has a full gas tank!")

class ElectricCar(Car) :
    def __init__(self, make, model, year) :
        super().__init__(make, model, year)
        self.batterySize = 70

    def desc_Battery(self) :
        print('this car has battery life of', self.batterySize)

    def fill_gas_tank(self) :
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

#You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class.
#Python will disregard the parent class method and only pay attention to the method you define in the child class.
#Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method.
#Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead.
#When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class.

tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
tesla.fill_gas_tank()
