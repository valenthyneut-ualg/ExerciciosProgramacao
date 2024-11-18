from random import random

from FourInARow.Board import Board

if __name__ == "__main__":
    board = Board()

    coords = (0, 0)
    for i in range(8):
        player = "X" if random() > .5 else "O"
        coords = board.play(player, 1)

    board.display()
    print(board.inWinState(coords))