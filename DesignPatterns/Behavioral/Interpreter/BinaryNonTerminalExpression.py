from AbstractExpression import AbstractExpression

from Context import Context

class BinaryNonTerminalExpression(AbstractExpression):

    def __init__(self, left_expression: AbstractExpression, right_expression: AbstractExpression, operator: str) -> None:
        self.left_expression = left_expression
        self.right_expression = right_expression
        self.operator = operator

    def interpret(self, context: Context):
        if (self.operator == '+'):
            return self.left_expression.interpret(context) + self.right_expression.interpret(context)
        elif (self.operator == '-'):
            return self.left_expression.interpret(context) - self.right_expression.interpret(context)
        elif (self.operator == '*'):
            return self.left_expression.interpret(context) * self.right_expression.interpret(context)
