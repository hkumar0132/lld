class Car:
    def __init__(self, brand, model):
        ''' 
            __brand makes it private: concept of encapsulation
        '''
        self.__brand = brand 
        self.__model = model

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    '''
        The variable __model can directly be accessed as a property -> object_name.model
    '''
    @property
    def model(self):
        return self.__model

    '''
        self.__model can be directly set using object_name.model = "XYZ"
    '''
    @model.setter
    def model(self, value):
        self.__model = value

    def full_name(self):
        return f'{self.__model} {self.__brand}'

c = Car("Tata", "Safari")

'''
    This throws error: 'Car' object has no attribute '__brand'. Did you mean: 'get_brand'?
'''
print(c.__brand)

# print(c.get_brand())
# print(c.get_model())
# print(c.model)

'''
    This line creates a new attribute __brand in the instance c, 
    it doesn't modify the private variable __brand defined in the class.
'''
c.__brand = "A"

# print(c.get_brand())
# print(c.__brand) -> throws error

c.model = "B"
print(c.model)