'''
    Method overriding is a way to achieve run-time polymorphism
    fuel_type has different implementation detail in child class Electric Car
    than parent class Car
'''

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand 
        self.__model = model
        '''
            or self.total_car += 1
        '''
        Car.total_car += 1

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
    
    def fuel_type(self):
        print("PETROL or DIESEL")

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

    def fuel_type(self):
        print("ELECTRIC")

ec = ElectricCar("Tesla", "X", 1000)
ec.fuel_type()

normal_car = Car("Tata", "Safari")
normal_car.fuel_type()

'''
    Count total number of objects created this way
'''
print(Car.total_car)


'''
    Another way but not recommended since you may 
    not need reference of this object
'''
print(normal_car.total_car)




'''
    THIS DOES NOT WORK IN PYTHON

    Method overloading: Same function name but different
    arguments
    Either number of arguments differ or type of arguments.
    This is compile-time polymorphism
'''


class A:
    def __init__(self) -> None:
        pass

    def sum(self, a, b, c):
        return a + b + c

    def sum(self, a, b):
        return a + b
    
    '''
        Only this will be available since
        it's declared at last
    '''
    def sum(self, *args):
        return sum(args)
    
a = A()
print(a.sum(1, 2))
print(a.sum(1, 2, 3))