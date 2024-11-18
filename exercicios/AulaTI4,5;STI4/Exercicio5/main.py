from random import random

from FourInARow.Board import Board

if __name__ == "__main__":
    board = Board()

    coords = board.play("X", 7)
    board.play("X", 6)
    board.play("X", 6)
    board.play("O", 5)
    board.play("O", 5)
    coords = board.play("X", 5)
    board.play("O", 4)
    board.play("O", 4)
    board.play("O", 4)
    board.play("X", 4)

    board.display()
    print(board.inWinState(coords))