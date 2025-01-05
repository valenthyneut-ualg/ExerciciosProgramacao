from random import randrange
from time import sleep
from typing import cast
from AbstractGame.AbstractController import AbstractController
from .Board import Board

class Controller(AbstractController):
	def __init__(self, playerCount: int):
		super().__init__("Jogo da Glória", Board(playerCount), playerCount)

		self.turnOrder = []
		self.playerEffects = []

	def rollTurnOrder(self):
		turnOrder = {}

		i = 0
		while len(turnOrder) < self.playerCount:
			turnRoll = randrange(0, 1000)
			if turnRoll not in turnOrder.values():
				turnOrder[i] = turnRoll
				i += 1

		sortedOrder = sorted(turnOrder.items(), key=lambda x: x[1])
		return sortedOrder

	def turn(self, player: int = -1) -> int | None:
		sleep(2)
		print("\n\n")
		print(str(self.board))

		if self.playerEffects[player] == "skip":
			print(f'Jogador {player + 1}, a tua rodada é passada à frente.')
			self.playerEffects[player] = None
			return

		try:
			moveAmount = int(input(f'Jogador {player + 1}, carregue no Enter para atirar os dados. '))
			print("Rodada manipulada.")
		except ValueError:
			rolls = [randrange(1, 6), randrange(1, 6)]
			rollSum = rolls[0] + rolls[1]
			moveAmount = rollSum
			sleep(.5)
			print("\n\n")
			print(f'Resultado: [{rolls[0]}][{rolls[1]}] = {rollSum}')

		effect, effectAmount, message = cast(Board, self.board).play(player, moveAmount)

		if effect:
			print(message)
			if effect == "move": cast(Board, self.board).play(player, effectAmount)
			elif effect == "skip": self.playerEffects[player] = "skip"
			elif effect == "reroll": return self.turn(player)

		print(f'Jogador {player + 1}, chegou à posição {cast(Board, self.board).state[player]}.')
		inWinState = cast(Board, self.board).inWinState()
		if inWinState[0]: return inWinState[1]

	def start(self):
		self.turnOrder = self.rollTurnOrder()
		self.playerEffects = [None] * self.playerCount
		playerOrder = ", ".join(map(lambda x: str(x[0] + 1), self.turnOrder))

		print("Ordem dos jogadores:", playerOrder)

		player = 0
		result = None

		while result is None:
			result = self.turn(self.turnOrder[player][0])

			player += 1
			if player > self.playerCount - 1: player = 0

		print(f'O jogador {result} ganhou!')