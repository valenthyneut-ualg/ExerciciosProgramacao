from random import random

from FourInARow.Board import Board

if __name__ == "__main__":
    board = Board()

    coords = board.play("X", 1)
    board.play("X", 2)
    board.play("X", 2)
    board.play("X", 3)
    board.play("X", 3)
    board.play("X", 3)
    board.play("O", 4)
    board.play("X", 4)
    board.play("X", 4)
    board.play("X", 4)

    board.display()
    print(board.inWinState(coords))