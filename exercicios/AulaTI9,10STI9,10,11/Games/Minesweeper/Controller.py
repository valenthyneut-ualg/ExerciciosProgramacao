from typing import cast, Literal, Dict, Any

from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from Games.Minesweeper.Board import Board


class Controller(AbstractController):
	def __init__(self, players: tuple[Player, ...]):
		players = players[:1]
		super().__init__(Board(players, 9), players, 1)

	def __pick_starting_pos(self):
		board: Board = cast(Board, self.board)
		print(board)
		print("Insira um par de coordenadas onde quer começar.")
		print("O primeiro número é a linha, o segundo a coluna.")
		print("Exemplo: 3, 8")

		coords = None
		while coords is None:
			temp = input("\n> ")

			try:
				parsed_coordinates = [int(coord) for coord in temp.split(",")]
				if len(parsed_coordinates) != 2:
					raise ValueError("Tem de inserir exatamente dois valores nas coordenadas.")

				coord_x, coord_y = parsed_coordinates
				if coord_x not in range(0, board.grid_size) or coord_y not in range(0, board.grid_size):
					raise ValueError(f'Os valores das coordenadas têm de estar entre 0 e {board.grid_size - 1}, inclusivo')

				coords = (coord_x, coord_y)
			except ValueError as error:
				print("Inseriu uma posição inválida.")
				print(error)

		board.init_mines(coords)
		board.play(coords, False)

	def start(self):
		board: Board = cast(Board, self.board)
		if len(board.mine_pos) == 0: self.__pick_starting_pos()

		print("\nInsira um par de coordenadas onde quer jogar.")
		print("O primeiro número é a linha, o segundo a coluna.")
		print("Exemplo: 3, 8")
		print("Adicione um F antes das coordenadas para marcar a coordenada com uma bandeira.")
		print("Exemplo: F2, 4")

		result = "ongoing"
		while result == "ongoing": result = self.turn()

		if result == "win":
			print("Conseguiu desarmar o campo de minas!")
			return board.players[0]
		else:
			print("Oops!.. Rebentou uma mina.")
			return None

	def turn(self) -> Literal["win", "loss", "ongoing"]:
		board: Board = cast(Board, self.board)
		print(board)

		state = board.current_state()
		if state != "ongoing": return state

		print()
		raw_pos = input("> ")

		if raw_pos[0].lower() == "f":
			flagged = True
			raw_pos = raw_pos[1:]
		else:
			flagged = False

		try:
			parsed_coordinates = [int(coord) for coord in raw_pos.split(",")]
			if len(parsed_coordinates) != 2:
				raise ValueError("Tem de inserir exatamente dois valores nas coordenadas.")

			coord_x, coord_y = parsed_coordinates
			if coord_x not in range(0, board.grid_size) or coord_y not in range(0, board.grid_size):
				raise ValueError(f'Os valores das coordenadas têm de estar entre 0 e {board.grid_size - 1}, inclusivo')

			coords = (coord_x, coord_y)
			result = board.play(coords, flagged)

			if result == "hit_mine":
				print(board)
				return "loss"
			elif result == "flagged":
				print("Marcou a coordenada com uma bandeira.")
			elif result == "unflagged":
				print("Retirou a bandeira da coordenada.")
		except ValueError as error:
			print("Inseriu uma posição inválida.")
			print(error)

		return "ongoing"

	def serialize(self) -> Dict[str, Any]:
		return {}