import numpy as np


class Board(object):

    def __init__(self, rows=3, cols=3):
        """
        Creates an environment for tictactoe.

        :param rows: the number of rows for the board.
        :param cols: the number of cols for the board.
        """
        self._rows = rows
        self._cols = cols

        self._board = np.zeros((rows, cols))

        self.player_x = 1
        self.player_o = -1

    def accept_move(self, row, col, player):
        """
        Update the board's state after a player takes a move.

        :param row: The selected row for a given play.
        :param col: The selected column for a given play.
        :param player: whose turn it is, either player_x or player_o
        """
        self._board[row, col] = player

    def available_moves(self):
        """
        Returns of all available moves remaining on the board.

        :return: A list of all available moves left on the board.
        """
        return np.argwhere(self._board == 0)

    def check_winner(self):
        """
        Checks the board to determine whether a player has won or not.

        :return: If no player has won, then 0 is returned. Otherwise, player_x or player_o is returned based off who
        won.
        """

        # Iterate across the players, checking for the win condition
        for player in [self.player_x, self.player_o]:
            # First check the rows
            rows = np.all(self._board == player, axis=1)
            cols = np.all(self._board == player, axis=0)

            # Then the two diagonals
            main_diagonal = np.all(np.diag(self._board) == player)
            alternate_diagonal = np.all(np.diag(np.fliplr(self._board)) == player)

            if np.any(rows) or np.any(cols) or np.any(main_diagonal) or np.any(alternate_diagonal):
                return player

        return 0

    def is_draw(self):
        return self.check_winner() == 0 and len(self.available_moves()) == 0

    def reset(self):
        """
        Reset's the board to the default state.
        """
        self._board = np.zeros((self._rows, self._cols))

    def __str__(self):
        to_print = ""
        print_dict = {
            0: ' ',
            self.player_x: 'X',
            self.player_o: 'O',
        }

        for col in range(self._cols):
            for row in range(self._rows):
                to_print += print_dict[self._board[row, col]] + (' | ' if row < self._rows-1 else '')
            # Add nice boarders
            to_print += '\n' + ('-'*9 + '\n' if col < self._cols-1 else '')

        return to_print


if __name__ == "__main__":
    board = Board()

    print(board)
    board.accept_move(0, 0, board.player_x)
    board.accept_move(0, 1, board.player_x)
    print("Winner: ", board.check_winner())
    board.accept_move(0, 2, board.player_x)
    board.accept_move(1, 1, board.player_o)
    print(board)

    print("Winner: ", board.check_winner())

    print(board.available_moves())