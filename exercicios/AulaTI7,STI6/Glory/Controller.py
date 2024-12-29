from random import randrange
from time import sleep

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

    def turn(self, player: int):
        sleep(2)
        print("\n\n")

        self.board.display()

        try:
            moveAmount = int(input(f'Jogador {player + 1}, carregue no Enter para atirar os dados. '))
            print("Rodada manipulada.")
        except ValueError:
            rolls = [randrange(1, 6), randrange(1, 6)]
            rollSum = rolls[0] + rolls[1]
            moveAmount = rollSum
            sleep(0.5)
            print("\n\n")
            print(f'Resultado: [{rolls[0]}][{rolls[1]}] = {rollSum}')

        message = self.board.move(player, moveAmount)
        if message: print(message)
        print(f'Jogador {player + 1}, chegou à posição {self.board.playerPositions[player]}!')

    def start(self):
        self.turnOrder = self.rollTurnOrder(2)
        playerOrder = ", ".join(map(lambda x: str(x[0] + 1), self.turnOrder))

        print("Ordem dos jogadores:", playerOrder)

        player = 0
        while True:
            self.turn(self.turnOrder[player][0])
            if 64 in self.board.playerPositions: break

            player += 1
            if player > len(self.turnOrder) - 1: player = 0

        print(f'Jogador {self.turnOrder[player][0] + 1}, ganhou!')