from abc import ABC, abstractmethod

enums/
from enum import Enum
class Operation(Enum):
    ADD='+',
    SUBTRACT='-'
    DIVISION='-'
    MULTIPLY='*'

class CalculationStrategy:
    @abstractmethod
    def calculate(a: float, b: float):
        pass

class SubCalculation(CalculationStrategy):
    def calculate(a: float, b: float):
        return a - b

class AddCalculation(CalculationStrategy):
    def calculate(a: float, b: float):
        return a + b
    
class DivisionCalculation(CalculationStrategy):
    def calculate(a: float, b: float):
        if b == 0:
            raise ValueError("Invalid division")
        return a // b    

exceptions/
class InvalidOperationException(Exception):
    def __init__(self, message='Operation not allowed'):
        super().__init__(message)

class CalulationStrategyFactory:
    operation_map = {
        Operation.ADD: AddCalculation,
        Operation.SUBTRACT: SubCalculation
    }

    @staticmethod
    def create(cls, op):
        if op not in cls.operation_map:
            raise InvalidOperationException()
        cls.operation_map[op]

class Calculator:
    def __init__(self, calculation_factory: CalulationStrategyFactory):
        self.calculation_factory = calculation_factory

    def calculate(self, a: float, b: float, op: Operation):
        operation_class = self.calculation_factory.create(op)
        return operation_class.calculate(a, b)