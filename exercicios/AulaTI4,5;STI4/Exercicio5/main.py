from FourInARow.Board import Board

if __name__ == "__main__":
    board = Board()

    board.play("X", 1)
    board.play("X", 2)
    board.play("X", 3)
    coords = board.play("X", 4)

    board.display()
    print(board.inWinState(coords))