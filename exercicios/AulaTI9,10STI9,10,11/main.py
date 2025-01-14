from json import loads, dumps
from os import _exit, remove
from os.path import exists
from typing import Dict

from pynput.keyboard import GlobalHotKeys, Listener

from AbstractGame.AbstractController import AbstractController
from AbstractGame.GameSpecification import GameSpecification
from AbstractGame.Player import Player

from Games.TicTacToe.Controller import Controller as TicTacToe
from Games.FourInARow.Controller import Controller as FourInARow
from Games.Glory.Controller import Controller as Glory
from Games.Hangman.Controller import Controller as Hangman
from Games.Minesweeper.Controller import Controller as Minesweeper

# Global variables
SAVEFILE_PATH = "save.json"

GAME: GameSpecification | None = None
GAME_INSTANCE: AbstractController | None = None
GAMES: list[GameSpecification] = [
	{ "title": "Jogo do galo", "min_player_count": 2, "controller": TicTacToe },
	{ "title": "Quatro em linha", "min_player_count": 2, "controller": FourInARow },
	{ "title": "Jogo da glória", "min_player_count": 2, "controller": Glory },
	{ "title": "Jogo da forca", "min_player_count": 1, "controller": Hangman },
	{ "title": "Campo de minas", "min_player_count": 1, "controller": Minesweeper }
]
PLAYERS: tuple[Player] | None

LISTENER: Listener | None = None

# Helper functions
def json_parse_aid(obj):
	if isinstance(obj, set):
		return list(obj)
	raise TypeError


def save():
	global GAME, PLAYERS
	print()

	player_data = tuple([player.serialize() for player in PLAYERS])
	if GAME is None: game_data = {}
	else: game_data = {
		GAME["title"]: {
			"controller_data": GAME_INSTANCE.serialize(),
			"board_data": GAME_INSTANCE.board.serialize()
		}
	}

	if exists(SAVEFILE_PATH):
		with open(SAVEFILE_PATH, "r") as save_file:
			existing_save_data: Dict = loads("".join(save_file.readlines()))
			existing_game_data: Dict | None = existing_save_data.get("game_data")
			if existing_game_data is not None:
				for title in existing_game_data.keys():
					if GAME is None or title != GAME["title"]: game_data[title] = existing_game_data.get(title)

	save_data = dumps({
		"players": player_data,
		"game_data": game_data
	}, indent=4, default=json_parse_aid)

	with open("save.json", "w") as save_file: save_file.writelines(save_data)
	print("Estado guardado.")

	_exit(0)


def setup_listener():
	global LISTENER

	print()
	listener = GlobalHotKeys({ "<ctrl>+s": save })
	listener.start()
	print("Carregue na combinação CTRL+S para guardar e sair do jogo.\n")


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


def get_players_from_save(save_data: Dict):
	global PLAYERS

	players: list[Player] = []
	save_players = save_data.get("players")
	for player in save_players:
		players.append(Player(player.get("name"), player.get("symbol")))

	PLAYERS = tuple(players)


def pick_game():
	global GAME, GAME_INSTANCE, GAMES, PLAYERS
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

	GAME_INSTANCE = GAME["controller"](PLAYERS)

# Main function block
def main():
	global SAVEFILE_PATH, GAME, GAME_INSTANCE, PLAYERS, LISTENER

	save_file_exists = exists(SAVEFILE_PATH)
	save_data: Dict | None = None

	if save_file_exists:
		print("Quer continuar a sessão de jogos anterior? Y/n")
		answer = input("> ").lower()

		print()
		if answer in ("y", "yes", "sim"):
			print("A continuar a sessão de jogos anterior...")
			with open(SAVEFILE_PATH, "r") as save_file:
				save_data = loads("".join(save_file.readlines()))
			get_players_from_save(save_data)
		elif answer in ("n", "no", "nao", "não"):
			print("A iniciar uma nova sessão de jogos..")
			remove(SAVEFILE_PATH)
			get_players_from_input()
		else:
			print("Resposta inválida. O programa irá parar.")
	else:
		get_players_from_input()

	try:
		while True:
			pick_game()

			if save_data is not None:
				game_data: Dict = save_data.get("game_data")
				game_save_data: Dict | None = game_data.get(GAME["title"])
				if game_save_data is not None:
					print("\nQuer continuar a sessão deste jogo? Y/n")
					answer = input("> ").lower()

					print()
					if answer in ("y", "yes", "sim"):
						print("A continuar da sessão anterior..")
						GAME_INSTANCE.deserialize(game_save_data.get("controller_data"))
						GAME_INSTANCE.board.deserialize(game_save_data.get("board_data"))
					else:
						print("A iniciar uma nova sessão..")
						game_data.pop(GAME["title"])
						save_data["game_data"] = game_data
						with open(SAVEFILE_PATH, "w") as save_file:
							save_file.writelines(dumps(save_data, indent=4, default=json_parse_aid))

			if LISTENER is None: setup_listener()
			winner = GAME_INSTANCE.start()

			print()
			for player in PLAYERS:
				cur_score = player.game_scores.get(GAME["title"])
				if cur_score is None: cur_score = 0
				player.game_scores[GAME["title"]] = cur_score

				if winner is not None and player.name == winner.name:
					player.game_scores[GAME["title"]] += 1

					total_score = 0
					for key in player.game_scores.keys(): total_score += player.game_scores[key]
					print(f'O jogador {player.name} tem {player.score[GAME["title"]]} pontos no jogo {GAME["title"]}, com {player.total_score} pontos no total.')

			GAME = None
			GAME_INSTANCE = None
	except KeyboardInterrupt:
		save()

if __name__ == "__main__": main()