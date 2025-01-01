'''
    Interfaces should be segregated in a way that a class does not need to implement
    a function unnecessarily
'''

'''
    Violation:
    Fish needs to implement give_birth unnecessarily
    while Human needs to implement swim and lay_eggs unnecessarily
'''

from abc import ABC, abstractmethod
class AnimalI(ABC):

    @abstractmethod
    def give_birth():
        pass

    @abstractmethod
    def swim():
        pass

    @abstractmethod
    def lay_eggs():
        pass

class Fish(AnimalI):
    def give_birth():
        raise Exception("Fish do not give birth directly")

'''
    RIGHT
'''

class MammalI(ABC):
    @abstractmethod
    def give_birth():
        pass

class Human(MammalI):
    def give_birth(self):
        pass

class MarineAnimalI(ABC):
    @abstractmethod
    def swim():
        pass

    def lay_eggs():
        pass

class Fish(abstractmethod):
    def swim(self):
        pass

    def lay_eggs(self):
        pass
