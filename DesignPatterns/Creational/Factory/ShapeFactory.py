from Shape import Circle, Diagonal, NullShape, Rectangle

class ShapeFactory:
    
    def get_shape(self, input):
        if input == "CIRCLE":
            return Circle()
        elif input == "RECTANGLE":
            return Rectangle()
        elif input == "DIAGONAL":
            return Diagonal()
        return NullShape()