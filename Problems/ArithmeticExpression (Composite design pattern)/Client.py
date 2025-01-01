from Number import Number
from IExpression import IExpression
from BinaryExpression import BinaryExpression
from Operators import Operators

class Client:

    '''
    
    5 * (5 + 2)

        *
        /\
    5      +
            /\
          5    2
    
    '''

    five = Number(5)
    two = Number(2)

    plus_op = BinaryExpression(five, two, Operators.ADD)
    parent_op = BinaryExpression(five, plus_op, Operators.MULTIPLY)

    print(parent_op.evaluate())