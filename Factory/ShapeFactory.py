from Shape.Circle import Circle
from Shape.Diagonal import Diagonal
from Shape.Rectangle import Rectangle
from Shape.NullShape import NullShape

class ShapeFactory:
    
    def get_shape(self, input):
        if input == "CIRCLE":
            return Circle()
        elif input == "RECTANGLE":
            return Rectangle()
        elif input == "DIAGONAL":
            return Diagonal()
        return NullShape()