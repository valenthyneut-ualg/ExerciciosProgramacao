from AbstractGame.GameSpecification import GameSpecification
from AbstractGame.Player import Player

from Games.TicTacToe.Controller import Controller as TicTacToe

# Global variables
GAME: GameSpecification | None = None
GAMES: list[GameSpecification] = [
	{ "title": "Jogo do galo", "min_player_count": 2, "controller": TicTacToe },
]
PLAYERS: tuple[Player] | None


# Helper functions
def get_players_from_input():
	global PLAYERS

	print("Insira o número de jogadores.\n"
		  "(Atenção, alguns jogos têm um número de jogadores fixo.)")

	player_count = 0

	while player_count == 0:
		try: player_count = int(input("> "))
		except ValueError: print("Número de jogadores inválido.\n")

	players = []
	takenSymbols: list[str] = []

	for i in range(player_count):
		print(f'\nInsira o nome do jogador {i + 1}.')
		name = input("> ")

		symbol_done = False
		while not symbol_done:
			print(f'\nInsira o símbolo do jogador {name} (máx.: 1 carácter).')
			symbol = input("> ")

			try:
				if int(symbol) in range(1, player_count + 1):
					print("Símbolo não pode ser igual a um número de jogador.")
					continue
			except ValueError: pass

			if len(symbol) > 1:
				symbol = symbol[0]
				print("Símbolo recortado ao primeiro carácter.")

			if symbol in takenSymbols:
				symbol = str(i + 1)
				print("Símbolo duplicado. Será utilizado o número do jogador.")

			players.append(Player(name, symbol))
			takenSymbols.append(symbol)
			symbol_done = True
			print()

	PLAYERS = tuple(players)


def pick_game():
	global GAME, GAMES, PLAYERS
	print()

	while GAME is None:
		print("Escolha um dos jogos seguintes.")
		for i in range(len(GAMES)): print(f'{i + 1} - {GAMES[i]["title"]}')

		try:
			game_choice = int(input("> ")) - 1
			if game_choice in range(0, len(GAMES)): GAME = GAMES[game_choice]
			else: raise ValueError
		except ValueError:
			print("Por favor, selecione apenas um jogo presente na lista.")

# Main function block
def main():
	global GAME, PLAYERS

	get_players_from_input()
	pick_game()

	GAME["controller"](PLAYERS).start()

if __name__ == "__main__": main()