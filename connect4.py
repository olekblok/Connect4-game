class Connect4:
    """Connect 4 game class.
    """
    ROWS = 6
    COLS = 7
    
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.current_player = 'X'

    def print_board(self) -> None:
        """Print the game board.
        """
        for row in self.board:
            print('|'.join(row))
            print('-' * self.COLS)
        print(' '.join([str(i) for i in range(self.COLS)]))

    def is_valid_location(self, col) -> bool:
        """Check if column is a valid location.

        Args:
            col (int): Column to check.

        Returns:
            bool: Returns True if the column is a valid location, False otherwise. 
        """
        return self.board[0][col] == ' '

    def get_next_open_row(self, col) -> int:
        """Get the next open row in the column.

        Args:
            col (int): Column to check.

        Returns:
            int: Row number of the next open row.
        """
        for r in range(self.ROWS-1, -1, -1):
            if self.board[r][col] == ' ':
                return r

    def drop_piece(self, row, col) -> None:
        """Drop a piece in the column.

        Args:
            row (int): Row to drop the piece.
            col (int): Column to drop the piece.
        """
        self.board[row][col] = self.current_player

    def switch_player(self) -> None:
        """Switch the current player.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def winning_move(self) -> bool:
        """Check if the current player has won.

        Returns:
            bool: Returns True if the current player has won, False otherwise.
        """
        # Check horizontal locations for win
        for c in range(self.COLS-3):
            for r in range(self.ROWS):
                if self.board[r][c] == self.current_player and \
                   self.board[r][c+1] == self.current_player and \
                   self.board[r][c+2] == self.current_player and \
                   self.board[r][c+3] == self.current_player:
                    return True

        # Check vertical locations for win
        for c in range(self.COLS):
            for r in range(self.ROWS-3):
                if self.board[r][c] == self.current_player and \
                   self.board[r+1][c] == self.current_player and \
                   self.board[r+2][c] == self.current_player and \
                   self.board[r+3][c] == self.current_player:
                    return True

        # Check positively sloped diagonals
        for c in range(self.COLS-3):
            for r in range(self.ROWS-3):
                if self.board[r][c] == self.current_player and \
                   self.board[r+1][c+1] == self.current_player and \
                   self.board[r+2][c+2] == self.current_player and \
                   self.board[r+3][c+3] == self.current_player:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.COLS-3):
            for r in range(3, self.ROWS):
                if self.board[r][c] == self.current_player and \
                   self.board[r-1][c+1] == self.current_player and \
                   self.board[r-2][c+2] == self.current_player and \
                   self.board[r-3][c+3] == self.current_player:
                    return True

        return False
