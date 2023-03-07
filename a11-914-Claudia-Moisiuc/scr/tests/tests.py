import unittest

from scr.repository.repository import Repository
from scr.service.service import Service


class DomainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = Repository()
        self.service = Service(self.repository)

    def test_drop_piece(self):
        self.repository.create_board()
        self.service.drop_piece(0, 3, 1)
        self.service.drop_piece(0, 5, 2)
        self.assertEqual(self.repository.board[0][3], 1)
        self.assertEqual(self.repository.board[0][5], 2)

    def test_valid_location(self):
        self.repository.create_board()
        self.service.drop_piece(0, 1, 1)
        self.service.drop_piece(1, 1, 2)
        self.service.drop_piece(2, 1, 1)
        self.service.drop_piece(3, 1, 2)
        self.service.drop_piece(4, 1, 1)
        self.service.drop_piece(5, 1, 2)
        self.assertEqual(self.service.valid_location(1), False)

    def test_get_next_row(self):
        self.repository.create_board()
        self.service.drop_piece(0, 1, 1)
        self.service.drop_piece(1, 1, 2)
        self.service.drop_piece(2, 1, 1)
        self.assertEqual(self.service.get_next_row(1), 3)

    def test_win(self):
        self.repository.create_board()
        self.service.drop_piece(0, 1, 1)
        self.service.drop_piece(1, 1, 1)
        self.service.drop_piece(2, 1, 1)
        self.service.drop_piece(3, 1, 1)
        self.assertEqual(self.service.win(1), True)

        self.service.drop_piece(0, 1, 2)
        self.service.drop_piece(0, 2, 2)
        self.service.drop_piece(0, 3, 2)
        self.service.drop_piece(0, 4, 2)
        self.assertEqual(self.service.win(2), True)

        self.service.drop_piece(1, 1, 3)
        self.service.drop_piece(2, 2, 3)
        self.service.drop_piece(3, 3, 3)
        self.service.drop_piece(4, 4, 3)
        self.assertEqual(self.service.win(3), True)

    def test_pick_best_move(self):
        self.repository.create_board()
        self.service.drop_piece(0, 1, 1)
        self.service.drop_piece(1, 1, 1)
        self.service.drop_piece(2, 1, 1)
        self.assertEqual(self.service.pick_best_move(2),1)