class Connect4:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * self.COLS)
        print(' '.join([str(i) for i in range(self.COLS)]))

    def is_valid_location(self, col):
        return self.board[0][col] == ' '

    def get_next_open_row(self, col):
        for r in range(self.ROWS-1, -1, -1):
            if self.board[r][col] == ' ':
                return r

    def drop_piece(self, row, col):
        self.board[row][col] = self.current_player

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def winning_move(self):
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
