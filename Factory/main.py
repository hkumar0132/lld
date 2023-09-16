from ShapeFactory import ShapeFactory

def main():
    shape = ShapeFactory()
    s = shape.get_shape("")
    s.draw()

if __name__ == "__main__":
    main()