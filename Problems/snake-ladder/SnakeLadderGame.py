from Board import Board
from Dice import Dice
from Player import Player


class SnakeLadderGame:
    def __init__(self, number_of_players, name_of_players, ladders, snakes):
        self.initialize_game(number_of_players, name_of_players, ladders, snakes)
        
    def initialize_game(self, number_of_players, name_of_players, ladders, snakes):
        self.board = Board()
        self.dice = Dice()
        self.players = []
        for i in range(0, number_of_players):
            self.players.append(Player(name_of_players[i], -1, -1))
            
        for i in range(0, len(snakes)):
            self.board.add_snake(snakes[i])
        
        for i in range(0, len(ladders)):
            self.board.add_ladder(ladders[i])
            
    def _check_if_winner(self, position):
        return position[0] == 9 and position[1] == 0
    
    def start_game(self):
        no_winner = True
        while no_winner:
            for i in range(0, len(self.players)):
                dice_value = self.dice.roll()
                position = self.players[i].get_position()
                new_position = self.board.move_player_position(position[0], position[1], dice_value)
                self.players[i].set_position(new_position[0], new_position[1])
                
                print(f'{self.players[i].get_name()} rolled a {dice_value} and moved from {position} to {new_position}')
                
                if self._check_if_winner(new_position):
                    no_winner = False
                    print(f'{self.players[i].get_name()} wins the game')
                    break
                    
                
                
            