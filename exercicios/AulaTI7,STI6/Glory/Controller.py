from random import randrange

from .Board import Board

class Controller:
    def __init__(self):
        self.board = Board()
        self.turnOrder = []

    @staticmethod
    def rollTurnOrder(playerCount: int):
        turnOrder = {}

        i = 0
        while len(turnOrder) < playerCount:
            turnRoll = randrange(0, 1000)
            if turnRoll not in turnOrder.values():
                turnOrder[i] = turnRoll
                i += 1

        sortedOrder = sorted(turnOrder.items(), key=lambda x: x[1])
        return sortedOrder

    def start(self):
        self.turnOrder = self.rollTurnOrder(2)
        playerOrder = ", ".join(map(lambda x: str(x[0] + 1), self.turnOrder))

        print("Ordem dos jogadores:", playerOrder)