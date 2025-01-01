from GameController import GameController


def main():
    chess = GameController(8)
    chess.start_game()
    print('Waiting for command')
    
if __name__ == "__main__":
    main()