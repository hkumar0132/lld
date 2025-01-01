'''
    The concept of hiding implementation details using interfaces or abstract
    classes is called abstraction
'''

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):

    def make_sound(self):
        return "woof"