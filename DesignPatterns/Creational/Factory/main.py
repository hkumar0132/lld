from ShapeFactory import ShapeFactory
from Shape import Shape

def main():
    shape = ShapeFactory()
    s = shape.get_shape("")
    s.draw()

if __name__ == "__main__":
    main()