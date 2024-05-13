from Context import Context
from AbstractExpression import AbstractExpression
from BinaryNonTerminalExpression import BinaryNonTerminalExpression
from TerminalExpression import TerminalExpression

class Client:

    context = Context()
    context.put("a", 1)
    context.put("b", 2)
    context.put("c", 3)
    context.put("d", 4)

    # a + b
    expression1 = BinaryNonTerminalExpression(
        TerminalExpression("a"),
        TerminalExpression("b"),
        '-'
    )

    # print(expression1.interpret(context))
    
    # (a + b) * (c + d)
    expression2 = BinaryNonTerminalExpression(
        BinaryNonTerminalExpression(
            TerminalExpression("a"),
            TerminalExpression("b"),
            '+'
        ),  
        BinaryNonTerminalExpression(
            TerminalExpression("c"),
            TerminalExpression("d"),
            '+'
        ),
        '*'
    )

    print(expression2.interpret(context))