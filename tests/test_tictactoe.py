import unittest
from tictactoe.board import Board


class MyTestCase(unittest.TestCase):

    def test_row_winner(self):
        board = Board()

        for x in range(board._cols):
            board.accept_move(x, 0, board.player_o)
            board.accept_move(x, 1, board.player_o)
            board.accept_move(x, 2, board.player_o)
            self.assertEqual(board.check_winner(), board.player_o, f"Error: player O should have won.")
            board.reset()

    def test_col_winner(self):
        board = Board()

        for y in range(board._rows):
            board.accept_move(0, y, board.player_x)
            board.accept_move(1, y, board.player_x)
            board.accept_move(2, y, board.player_x)
            self.assertEqual(board.check_winner(), board.player_x, f"Error: player X should have won.")
            board.reset()

    def test_diagonal_winner(self):
        board = Board()

        # Main diagonal
        for x in range(board._rows):
            board.accept_move(x, x, board.player_o)

        self.assertEqual(board.check_winner(), board.player_o)

        board.reset()

        # Alternate diagonal
        for x in range(board._rows):
            board.accept_move(board._cols - 1 - x, x, board.player_o)

        self.assertEqual(board.check_winner(), board.player_o)

    def test_draw(self):
        board = Board()
        board.accept_move(0, 0, board.player_o)
        board.accept_move(0, 1, board.player_x)
        board.accept_move(0, 2, board.player_o)
        board.accept_move(1, 0, board.player_x)
        board.accept_move(1, 1, board.player_x)
        board.accept_move(1, 2, board.player_o)
        board.accept_move(2, 0, board.player_x)
        board.accept_move(2, 1, board.player_o)
        board.accept_move(2, 2, board.player_x)
        print(board)
        self.assertEqual(board.is_draw(), True)


if __name__ == '__main__':
    unittest.main()
