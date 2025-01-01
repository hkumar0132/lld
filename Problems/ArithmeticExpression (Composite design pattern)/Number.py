from IExpression import IExpression

class Number(IExpression):

    def __init__(self, value) -> None:
        self.value = value

    def evaluate(self):
        return self.value