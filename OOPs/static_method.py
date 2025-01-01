'''
    Static methods are methods of class
    and not accessible by objects
'''

class Car:

    def __init__(self):
        pass
    
    @staticmethod
    def general_description():
        return "This is a car"
    
class ElectricCar(Car):
    pass


'''
    In python, it can be accessed using objects
    also 
'''
tesla = ElectricCar()
print(tesla.general_description())
c = Car()
print(c.general_description())


print(Car.general_description())