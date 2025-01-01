from IExpression import IExpression
from Operators import Operators

class BinaryExpression(IExpression):

    def __init__(self, left_expression: IExpression, right_expression: IExpression, operator: Operators) -> None:
        self.left_expression = left_expression
        self.right_expression = right_expression
        self.operator = operator

    def evaluate(self):
        if self.operator == Operators.ADD:
            return self.left_expression.evaluate() + self.right_expression.evaluate()
        elif self.operator == Operators.MINUS:
            return self.left_expression.evaluate() - self.right_expression.evaluate()
        elif self.operator == Operators.MULTIPLY:
            return self.left_expression.evaluate() * self.right_expression.evaluate()
        elif self.operator == Operators.DIVIDE:
            return self.left_expression.evaluate() / self.right_expression.evaluate()