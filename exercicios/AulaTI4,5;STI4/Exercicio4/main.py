from TicTacToe.Board import Board

if __name__ == "__main__":
    board = Board()
    board.play("X", 1, 1)
    board.play("X", 2, 1)
    board.play("X", 3, 1)
    board.display()
    print(board.inWinState())