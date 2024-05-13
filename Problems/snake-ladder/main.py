from Ladder import Ladder
from Snake import Snake
from SnakeLadderGame import SnakeLadderGame


def main():
    snake1 = Snake([5,0], [0,0])
    snake2 = Snake([7,1], [1,1])
    snake3 = Snake([9,8], [6,5])
    snake4 = Snake([8,8], [8,7])
    
    ladder1 = Ladder([0,0], [7,8])
    ladder2 = Ladder([1,1], [5,5])
    ladder3 = Ladder([6,7], [6,9])
    ladder4 = Ladder([9,1], [9,9])
    
    game = SnakeLadderGame(2, ['Himanshu', 'ABC'], [ladder1, ladder2, ladder3, ladder4], [snake1, snake2, snake3, snake4])
    game.start_game()

if __name__ == "__main__":
    main()