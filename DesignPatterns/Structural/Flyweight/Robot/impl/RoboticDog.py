from Robot import IRobot

class RoboticDog(IRobot):
    def __init__(self, graphic, body_type) -> None:
        self.__graphic = graphic
        self.__body_type = body_type

    def get_type(self):
        return self.__graphic
    
    def get_body_type(self):
        return self.__body_type
    
    def display(self, x: int, y: int):
        print(x, y)