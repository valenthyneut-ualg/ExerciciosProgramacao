from FourInARow.Board import Board

if __name__ == "__main__":
    board = Board()
    board.play("X", 1)
    board.play("O", 1)
    board.play("X", 2)
    board.play("O", 7)
    board.display()