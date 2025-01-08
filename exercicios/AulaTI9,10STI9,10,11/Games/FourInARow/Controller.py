from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from .Board import Board
from typing import cast

class Controller(AbstractController):
	def __init__(self, players: list[Player]):
		super().__init__("Quatro em linha", Board(players), 2)
		self.curPlayer = players[0]
		self.playerTurn = 0
		self.lastPlayedCoords: tuple[int, int] = (1, 1)

	def start(self):
		print("Insira o número da coluna onde quer colocar a sua peça.")

		result = "ongoing", None
		while result[0] == "ongoing":
			result = self.turn()

		print()
		if result[0] == "draw": print("Empate!")
		elif result[0] == "win": print(f'O jogador "{result[1]}" ganhou!')

	def turn(self) -> tuple[str, Player] | tuple[str, None]:
		print()
		print(self.board)

		player = cast(Board, self.board).inWinState(self.lastPlayedCoords)
		inWinState = player is not None
		if inWinState: return "win", player

		emptySpaces = 0
		for x in cast(list[list[str]], self.board.state):
			for y in x: emptySpaces += y.count(" ")

		if emptySpaces == 0: return "draw", None

		rawInput = input(f'[{self.curPlayer.symbol}] > ')
		try:
			column = int(rawInput)
			if column not in range(1, 9): raise ValueError("O número da coluna tem de estar compreendido entre 1 e 8, inclusivo.")

			self.lastPlayedCoords = cast(Board, self.board).play(self.curPlayer, column)
			self.playerTurn += 1
			if self.playerTurn >= self.playerCount: self.playerTurn = 0
			self.curPlayer = self.board.players[self.playerTurn]
		except ValueError as error:
			print("Inseriu uma posição inválida.")
			print(error)

		return "ongoing", None