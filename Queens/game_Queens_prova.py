class ChessBoard:
    def __init__(self):
        self.board = [['.' for _ in range(8)] for _ in range(8)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def place_queen(self, row, col):
        self.board[row][col] = 'Q'

    def remove_queen(self, row, col):
        self.board[row][col] = '.'

    def is_safe(self, row, col):
        for i in range(8):
            if self.board[row][i] == 'Q' or self.board[i][col] == 'Q':
                return False
        for i in range(8):
            for j in range(8):
                if abs(row - i) == abs(col - j) and self.board[i][j] == 'Q':
                    return False
        return True

    def solve(self, row=0):
        if row == 8:
            self.print_board()
            return True
        for col in range(8):
            if self.is_safe(row, col):
                self.place_queen(row, col)
                if self.solve(row + 1):
                    return True
                self.remove_queen(row, col)
        return False

if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.solve()
