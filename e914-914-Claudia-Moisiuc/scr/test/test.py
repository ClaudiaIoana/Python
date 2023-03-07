import unittest

from scr.repository.repository import Repository
from scr.service.service import Service


class Fire(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = Repository()
        self.service = Service(self.repository)

    def test_fire_valid(self):
        self.__game_board = self.repository.create_board()
        self.__game_board[4][2] = '*'
        self.assertEqual(self.service.fire_valid(4, 2), True)
        self.__game_board[5][2] = '-'
        self.assertEqual(self.service.fire_valid(5, 2), True)

    def test_fire(self):
        self.__game_board = self.repository.create_board()
        self.__game_board[5][2] = '-'
        self.assertEqual(self.service.fire(5, 2),'not hit')
        self.__game_board[5][2] = ' '
        self.assertEqual(self.service.fire(5, 2), 'not hit')

#