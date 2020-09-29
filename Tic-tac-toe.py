import copy

class Board:
    """simple tic-tac-toe board"""
    def __init__(self, board=None):
        if board:
            self.board = copy.deepcopy(board)
        else:
            self.board = [[' '] * 3 for _ in range(3)]
    def place(self, row, col, what):
        """produce a new board with row and col set to a symbol. Return None if
        some symbol already set."""
        if self.board[row][col] == ' ':
            newboard = Board(self.board)
            newboard[row][col] = what
            return newboard
    def __getitem__(self, key):
        return self.board[key]
    def __repr__(self):
        separator = "\n---+---+---\n "
        return " " + separator.join([" | ".join(row) for row in self.board])
    def spaces(self):
        """tell how many empty spots on the board"""
        return sum(1 for i in range(3) for j in range(3) if self[i][j] == ' ')
    def won(self):
        """check winner. Return the winner's symbol or None"""
        # check rows
        for row in self.board:
            if row[0] != ' ' and all(c==row[0] for c in row):
                return row[0]
        # check cols
        for n in range(3):
            if self.board[0][n] != ' ' and all(self.board[i][n] == self.board[0][n] for i in range(3)):
                return self.board[0][n]
        # check diag
        if self.board[0][0] != ' ' and all(self.board[n][n] == self.board[0][0] for n in range(3)):
            return self.board[0][0]
        if self.board[0][2] != ' ' and all(self.board[n][2-n] == self.board[0][2] for n in range(3)):
            return self.board[0][2]

def play():
    "auto play tic-tac-toe"
    game = Board()
    player = 'X'
    # loop until the game is done
    print(game)
    while not game.won():
        opponent = 'O' if player == 'X' else 'X'
        while True:
            userin = input("Player %s, input coordinate (0-2, 0-2):" % player)
            nums = "".join(c if c.isdigit() else ' ' for c in userin).split()
            if len(nums) != 2:
                continue
            nums = [int(n) for n in nums]
            if not all(0 <= n <= 2 for n in nums):
                continue
            nextstep = game.place(nums[0], nums[1], player)
            if nextstep:
                game = nextstep
                break
        print()
        print("%s move:" % player)
        print(game)
        player = opponent
    winner = game.won()
    print()
    if not winner:
        print("Tied")
    else:
        print("%s has won" % winner)
while True:
  play()
