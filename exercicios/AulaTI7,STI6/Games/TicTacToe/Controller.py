from ..AbstractController import AbstractController
from .Board import Board

class Controller(AbstractController):
	def __init__(self):
		super().__init__(2)
		
		self.board = Board()
		self.turnPlayer = True
		self.turnPlayerChar = "X"

	def turn(self) -> tuple[int, str] | None:
		print()

		self.turnPlayerChar = "X" if self.turnPlayer else "O"
		self.board.display()

		inWinState, player = self.board.inWinState()
		if inWinState: return 1, player

		if self.board.state.count(" ") == 0: return 0, ""

		print()
		gameInput = input(f'[{self.turnPlayerChar}] > ')

		try:
			coordinates = [int(n) for n in gameInput.split(", ")]
			if len(coordinates) != 2: 
				raise ValueError("Apenas pode inserir dois valores nas coordenadas!")

			if coordinates[0] not in range(1, 4) or coordinates[1] not in range(1, 4):
				raise ValueError("Os números das coordenadas têm de estar compreendidas entre 1 e 3! (inclusivo)")
			
			self.board.placePiece(self.turnPlayerChar, coordinates[0], coordinates[1])
			self.turnPlayer = not self.turnPlayer
		except ValueError as error:
			print("Inseriu uma posição inválida!")
			print(error)
		
		return None

	def start(self):
		print("Insira um par de coordenadas separado por vírgula onde:")
		print("O primeiro número é a linha e o segundo a coluna.")
		print("Exemplo: 2, 3")

		result = None
		while result == None:
			result = self.turn()

		if result[0] == 0: print("Empate!")
		else: print(f'O jogador [{result[1]}] ganhou!')