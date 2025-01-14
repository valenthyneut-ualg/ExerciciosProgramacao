from random import choice, randrange
from time import sleep
from typing import Literal, cast, Dict, Any

from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from Games.Glory.Board import Board

class Controller(AbstractController):
	def __init__(self, players: tuple[Player, ...]):
		super().__init__(Board(players), players, 2)

		temp_turn_order: list[int] = []
		while len(temp_turn_order) != len(players):
			difference = list(set(temp_turn_order).symmetric_difference(set(range(self.player_count))))
			temp_turn_order.append(choice(difference))

		self.turn_order: tuple[int, ...] = tuple(temp_turn_order)
		self.cur_player: Player = players[self.turn_order[0]]
		self.player_turn = 0
		self.player_effects: list[str | None] = [None] * self.player_count

	def start(self):
		player_order = []
		for i in self.turn_order:
			player_order.append(self.board.players[i].symbol)

		player_order_string = ", ".join(player_order)

		print("Ordem dos jogadores:", player_order_string)

		result = "ongoing", None
		while result[0] == "ongoing":
			result = self.turn()

			self.player_turn += 1
			if self.player_turn >= self.player_count: self.player_turn = 0
			self.cur_player = self.board.players[self.turn_order[self.player_turn]]

		print()
		if result[0] == "win": print(f'O jogador "{result[1].name}" ganhou!')

	def turn(self) -> tuple[Literal["ongoing", "win"], Player | None]:
		board: Board = cast(Board, self.board)
		sleep(2)
		print("\n\n")
		print(board)

		if self.player_effects[self.player_turn] == "skip":
			print(f'Jogador {self.cur_player.symbol}, a sua rodada é passada à frente.')
			self.player_effects[self.player_turn] = None
			return "ongoing", None

		try:
			move_amount = int(input(f'Jogador {self.cur_player.symbol}, carregue no Enter para atirar os dados. '))
			print("Rodada manipulada.")
		except ValueError:
			rolls = [randrange(1, 6), randrange(1, 6)]
			roll_sum = sum(rolls)
			move_amount = roll_sum
			sleep(.5)

			print("\n\n")
			print(f'Resultado: [{rolls[0]}][{rolls[1]}] = {roll_sum}')

		move_result = board.play(self.cur_player, move_amount)

		if move_result is not None:
			effect, effect_amount, message = move_result
			print(message)
			if effect == "move": board.play(self.cur_player, effect_amount)
			elif effect == "skip": self.player_effects[self.player_turn] = "skip"
			elif effect == "reroll": return self.turn()

		print(f'Jogador {self.cur_player.symbol}, chegou à posição {board.player_positions[self.player_turn]}.')
		state, player = board.current_state()
		if state == "win": return "win", self.cur_player

		return "ongoing", None

	def serialize(self) -> Dict[str, Any]:
		return {
			"turn_order": self.turn_order,
			"player_turn": self.player_turn,
			"player_effects": self.player_effects
		}

	def deserialize(self, data: Dict[str, Any]) -> None:
		super().deserialize(data)
		self.cur_player = self.board.players[self.player_turn]