from json import loads

from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from .Board import Board
from typing import cast
from random import choice, randrange
from time import sleep

class Controller(AbstractController):
	def __init__(self, players: list[Player]):
		super().__init__("Jogo da glória", Board(players), len(players), 2)

		self.turnOrder: list[int] = []
		while len(self.turnOrder) != len(players):
			# Create an array containing every index NOT in self.turnOrder
			# and pick a (somewhat) random element from it
			difference = list(set(self.turnOrder).symmetric_difference(set(range(self.playerCount))))
			self.turnOrder.append(choice(difference))

		self.curPlayer = players[self.turnOrder[0]]
		self.playerTurn = 0
		self.playerEffects: list[str | None] = [None] * self.playerCount

	def start(self):
		playerOrder = []
		for index in self.turnOrder:
			playerOrder.append(self.board.players[index].symbol)
		playerOrder = ", ".join(playerOrder)

		print("Ordem dos jogadores:", playerOrder)

		result = "ongoing", None
		while result[0] == "ongoing":
			result = self.turn()

			self.playerTurn += 1
			if self.playerTurn >= self.playerCount: self.playerTurn = 0
			self.curPlayer = self.board.players[self.turnOrder[self.playerTurn]]

		print()
		if result[0] == "win": print(f'O jogador "{result[1]}" ganhou!')

	def turn(self) -> tuple[str, Player] | tuple[str, None]:
		sleep(2)
		print("\n\n")
		print(self.board)

		if self.playerEffects[self.playerTurn] == "skip":
			print(f'Jogador {self.curPlayer.symbol}, a sua rodada é passada à frente.')
			self.playerEffects[self.playerTurn] = None
			return "ongoing", None

		try:
			moveAmount = int(input(f'Jogador {self.curPlayer.symbol}, carregue no Enter para atirar os dados. '))
			print("Rodada manipulada.")
		except ValueError:
			rolls = [randrange(1, 6), randrange(1, 6)]
			rollSum = sum(rolls)
			moveAmount = rollSum
			sleep(.5)
			print("\n\n")
			print(f'Resultado: [{rolls[0]}][{rolls[1]}] = {rollSum}')

		moveResult = cast(Board, self.board).play(self.curPlayer, moveAmount)

		if moveResult is not None:
			effect, effectAmount, message = moveResult
			print(message)
			if effect == "move": cast(Board, self.board).play(self.curPlayer, effectAmount)
			elif effect == "skip": self.playerEffects[self.playerTurn] = "skip"
			elif effect == "reroll": return self.turn()

		print(f'Jogador {self.curPlayer.symbol}, chegou à posição {cast(Board, self.board).state[self.playerTurn]}.')
		inWinState = cast(Board, self.board).inWinState()
		if inWinState is not None: return "win", self.curPlayer

		return "ongoing", None

	def serialize(self):
		return {
			"turnOrder": self.turnOrder,
			"playerCount": self.playerCount,
			"playerTurn": self.playerTurn,
			"playerEffects": self.playerEffects
		}

	@staticmethod
	def deserialize(rawData: str, players: list[Player] = None):
		try:
			parsedData = loads(rawData)

			hasValidTurnOrder = hasattr(parsedData, "turnOrder") and parsedData.turnOrder is list[int]
			hasValidPlayerCount = hasattr(parsedData, "playerCount") and parsedData.playerCount is int
			hasValidPlayerTurn = hasattr(parsedData, "playerTurn") and parsedData.playerTurn is int
			hasValidPlayerEffects = hasattr(parsedData, "playerEffects") and parsedData.playerEffects is list[str | None]

			if hasValidTurnOrder and hasValidPlayerCount and hasValidPlayerTurn and hasValidPlayerEffects:
				if parsedData.playerCount != len(players):
					raise ValueError("Nº de jogadores não coincidem!")

				controller = Controller(players)

				controller.turnOrder = parsedData.playerTurn
				controller.playerCount = parsedData.playerCount
				controller.playerTurn = parsedData.playerTurn
				controller.curPlayer = players[controller.turnOrder[controller.playerTurn]]
				controller.playerEffects = parsedData.playerEffects
				return controller
		except AttributeError as error:
			print("Ocorreu um erro a ler um save do jogo!")
			print(error)
		except ValueError as error:
			print("Ocorreu um erro a preparar o jogo!")
			print(error)