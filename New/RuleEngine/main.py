'''
Requirements:
1. System supports creating rules
    - simple : a > b or a = b
    - composite: [a > b, AND, a = b]
2. Allow certain actions after rule evaluation

'''

Core entities:

1. Operation
    - EqualOperation
    - GreaterThanOperation
    - LessThanOrEqualToOperation
2. Rule
3. Condition
    - SimpleCondition
    - CompositeCondition
4. RuleEngine

Design:

from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def apply(self):
        pass

class EqualOperation(Operation):
    def apply(self, left, right):
        return left == right

class GreaterThanOperation(Operation):
    def apply(self, left, right):
        return left > right
        
class Condition(ABC):
    @abstractmethod
    def evaluate(self):
        pass

# age, >, 23
class FieldCondition(Condition):
    def __init__(self, field, operation: Operation, value):
        self.field = field
        self.operation = operation
        self.value = value

    # { "age": 18}
    def evaluate(self, data: dict):
        return self.operation.apply(data.get(self.field), self.value)
    

enums/
from enum import Enum
class JOIN_TYPE(Enum):
    AND='AND'
    OR='OR'


# List[age, >, =]

from typing import List
class CompositeCondition(Condition):
    def __init__(self, conditions: List[Condition], join_type: JOIN_TYPE):
        self.conditions = conditions
        self.join_type = join_type

    def evaluate(self, data: dict):
        result = [condition.evaluate(data) for condition in self.conditions]
        return all(result) if self.join_type == "AND" else any(result)
    
class Rule:
    def __init__(self, condition: Condition, action):
        self.condition = condition
        self.action = action

    def evaluate(self, data: dict):
        return self.action if self.conditions.evaluate(data)
    
class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def evaluate(self, data: dict):
        actions = []
        for rule in self.rules:
            if rule.evaluate(data):
                actions.append(rule.action)
        return actions

def main():
    cond1 = FieldCondition("age", GreaterThanOperation(), 18)
    cond2 = FieldCondition("country", EqualOperation(), "IN")

    composite_condition = CompositeCondition([cond1, cond2], "AND")

    rule = Rule(composite_condition, "CAN VOTE")

    rule_engine = RuleEngine()
    rule_engine.add_rule(rule)
    rule_engine.evaluate({ "age": 19, "country": "IN" })

main()