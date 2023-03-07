import numpy as np
import texttable


class Repository:
    def __init__(self):
        self.__board = self.create_board()

    def create_board(self):
        board = np.zeros((6,7))
        return board

    def get_texttable(self):
        table = texttable.Texttable(0)
        for row in self.__board:
            table.add_row(row)
        return table

    @property
    def board(self):
        return self.__board
