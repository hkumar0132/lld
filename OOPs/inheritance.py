class Car:

    def __init__(self, brand, model):
        self.__brand = brand 
        self.__model = model

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def model(self, value):
        self.__model = value

class ElectricCar(Car):

    def __init__(self, brand, name, battery_size):
        super().__init__(brand, name)
        self.__battery_size = battery_size

    @property
    def battery_size(self):
        return self.__battery_size
    
    @battery_size.setter
    def battery_size(self, value):
        self.__battery_size = value

ec = ElectricCar("Tesla", "X", 1000)
print(ec.battery_size)
ec.battery_size = 1
print(ec.battery_size)

'''
    Multiple inheritance: One child class can inherit from
    multiple parent classes simultaneously
'''

class Battery:
    def get_engine(self):
        print("Battery")

class Engine:
    def get_engine(self):
        print("Engine")

class Tesla(Battery, Engine, Car):
    pass

t = Tesla("Tesla", "Y")
# t.get_battery()
t.get_engine()
print(t.model)