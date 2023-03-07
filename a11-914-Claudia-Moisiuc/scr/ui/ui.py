import random

import numpy as np

from scr.repository.validators import WrongInputError


class UI:
    def __init__(self, service, repository):
        self.__service = service
        self.__repository = repository

    def valid_game(self):
        """the function makes the move and puts them on the board"""
        game_over = False
        turn = random.randint(0, 1)
        while not game_over:
            if turn == 0:
                col = input("Player 1 turn (0-6):")
                if col < '0' or col > '6':
                    print(WrongInputError("*The input is not valid.*"))
                    turn = turn - 1
                elif not self.__service.valid_location(int(col)):
                    print(WrongInputError("*The input is not valid.*"))
                    turn = turn - 1
                else:
                    col = int(col)
                    if self.__service.valid_location(col):
                        row = self.__service.get_next_row(col)
                        self.__service.drop_piece(row, col, 1)
                    if self.__service.win(1):
                        print('PLAYER 1 WINS!!')
                        game_over = True
            else:
                col = self.__service.pick_best_move(2)
                if self.__service.valid_location(col):
                    row = self.__service.get_next_row(col)
                    self.__service.drop_piece(row, col, 2)
                if self.__service.win(2):
                    print('PLAYER 2 WINS!!')
                    game_over = True

                print("Pleyer 2 moved on column ", col)
            self.print_board()

            turn = turn + 1
            turn = turn % 2

    def print_board(self):
        print(self.__repository.get_texttable().draw())

