'''
    If class B is a subtype of class A, then we should be able to replace object of
    A with object of B without throwing any error
    or simply child class should extend the capability of parent class and not narrow
    it down
'''

class Animal:

    def give_birth(self):
        pass

    def swim(self):
        pass


class Fish(Animal):

    def give_birth(self):
        raise Exception("Fish does not give birth")

    def swim(self):
        pass

animal = Animal()
print(animal.give_birth())

fish = Fish()

'''
    Replacing animal object with fish object
'''
print(fish.give_birth())

