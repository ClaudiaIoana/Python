import numpy as np
import texttable


class Repository:
    def __init__(self):
        self.__board = self.create_board()
        self.__game_board = self.create_board()

    def create_board(self):
        board = [[' ']*8 for i in range (7)]
        for i in range (0, 7):
            board[i][0] = i+1
        board[3][4]='E'
        return board

    def get_texttable(self):
        table = texttable.Texttable(0)
        table.add_row([' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G'])
        for row in self.__board:
            table.add_row(row)
        return table

    def get_cheat(self):
        table = texttable.Texttable(0)
        table.add_row([' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G'])
        for row in self.__game_board:
            table.add_row(row)
        return table

    @property
    def board(self):
        return self.__board

    @property
    def game_board(self):
        return self.__game_board

#