from Directions import Directions

class DirectionFactory:
    def get_direction(self, direction):
        if direction == 0:
            return Directions.LEFT
        elif direction == 1:
            return Directions.RIGHT
        elif direction == 2:
            return Directions.TOP
        elif direction == 3:
            return Directions.BOTTOM
        else:
            pass
            # print('\nInvalid Direction')