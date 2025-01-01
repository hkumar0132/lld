from typing import List

from models import IBoardEntity, IPlayer, IDice, BoardEntityType
from Board import Board
from OneToSixDice import OneToSixDice

class Game:

    def __init__(self, N, entities, dices: List[IDice]) -> None:
        self.board = Board()
        self.players : List[IPlayer] = []
        self.dices = dices
        self.N = N
        self.entities : List[IBoardEntity] = entities
        self.__initialize_game()


    def __initialize_game(self):
        self.board.initialize_board(self.N, self.entities)

    def __get_new_position(self, current_cell: List[int], move_position: int):
        '''
            [
            [(0, 0), (0, 1), (0, 2)...],
            [(1, 0), (1, 2), (1, 3)...],
            [],
            [],
            [],
            [],
            [],
        '''

        row, col = current_cell
        if row % 2 == 1:
            # Left to right
            remaining_in_row = (self.N - col - 1)
            if move_position <= remaining_in_row:
                col += move_position
            else:
                row = max(0, row - 1)
                col = max(0, move_position - remaining_in_row)
        else:
            if col - move_position >= 0:
                col -= move_position
            else:
                row = max(0, row - 1)
                col = max(0, move_position - col)
        
        return [row, col]

    def __is_winner(self, cell: List[int]):
        return (cell[0] == 0 and cell[1] == 0)
    
    def __translate_position(self, position: List[int]):
        # return position        
        '''
            [
            [(0, 0), (0, 1), (0, 2)...],
            [(1, 0), (1, 2), (1, 3)...],
            [],
            [],
            [],
            [(8, 0), (), ()...., ()], -> [20, ....12, 11]
            [(9, 0), (9, 1), (9, 2),...., (9, 9)], -> [1, 2, 3..., 10]
        '''
        return position
        if position[0]%2 == 1:
            return (10 - position[0]) * 10 - 9 + position[1]
        else:
            return (10 - position[0]) * 10 - position[1]
    
    def __logger(self, player: IPlayer, position, new_position):
        print(f"Player Name: {player.get_player_name()}, id: {player.get_player_id()} moved from {self.__translate_position(position)} to {self.__translate_position(new_position)}")

    def add_player(self, player: IPlayer):
        player.set_position([self.N - 1, 0])
        self.players.append(player)

    def start_game(self):
        winner = False
        while not winner:
            for player in self.players:
                position = player.get_position()
                move_position = 0
                for dice in self.dices:
                    move_position += dice.roll_dice()

                print(f"Player {player.get_player_name()} rolled: {move_position}")

                new_position = self.__get_new_position(position, move_position)

                current_obj : IBoardEntity = self.board.get_object_at_cell(new_position)
                if not current_obj:            
                    player.set_position(new_position)       
                    self.__logger(player, position, new_position)
                    
                    if (self.__is_winner(new_position)):
                        print(f"Player Name: {player.get_player_name()}, id: {player.get_player_id()} has won the game")
                        winner = True
                        break
                else:
                    updated_position = current_obj.get_tail()

                    self.__logger(player, position, new_position)

                    if current_obj.get_type() == BoardEntityType.SNAKE:
                        print(f"Snake bite at {self.__translate_position(position)}, down to {self.__translate_position(updated_position)}")
                    elif current_obj.get_type() == BoardEntityType.LADDER:
                        print(f"Ladder at {self.__translate_position(position)}, up to {self.__translate_position(updated_position)}")

                    player.set_position(updated_position)

                    if (self.__is_winner(updated_position)):
                        print(f"Player Name: {player.get_player_name()}, id: {player.get_player_id()} has won the game")
                        winner = True
                        break