from AbstractExpression import AbstractExpression
from Context import Context

class TerminalExpression(AbstractExpression):

    def __init__(self, string_value) -> None:
        self.string_value = string_value

    def interpret(self, context: Context):
        return context.get(self.string_value)
