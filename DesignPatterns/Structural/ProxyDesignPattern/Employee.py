from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def create():
        pass

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def delete():
        pass