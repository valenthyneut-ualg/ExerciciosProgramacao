from json import loads, dumps
from os import remove, _exit
from os.path import exists
from typing import Dict

from pynput.keyboard import GlobalHotKeys, Listener

from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from Games.FourInARow.Controller import Controller as FourInARow
from Games.Glory.Controller import Controller as Glory
from Games.Hangman.Controller import Controller as Hangman
from Games.TicTacToe.Controller import Controller as TicTacToe

listener: Listener | None = None

game: AbstractController | None = None
players: list[Player] = []

def setupListener():
	global listener

	print()
	listener = GlobalHotKeys({ "<ctrl>+s": save })
	listener.start()
	print("Carregue na combinação CTRL+S para guardar e sair do jogo.\n")

def save():
	global game, players
	print()

	playerData = [player.serialize() for player in players]
	if game is None:
		gameData = {}
	else:
		gameData = {
			game.title: {
				"controllerData": game.serialize(),
				"boardData": game.board.serialize()
			}
		}

	if exists("save.json"):
		with open("save.json", "r") as saveFile:
			existingSaveData: Dict = loads("".join(saveFile.readlines()))
			existingGameData: Dict | None = existingSaveData.get("gameData")
			if existingGameData is not None:
				for title in existingGameData.keys():
					if game is None or title != game.title:
						gameData[title] = existingGameData.get(title)

	saveData = dumps({
		"players": playerData,
		"gameData": gameData
	}, indent=4)

	with open("save.json", "w") as saveFile: saveFile.writelines(saveData)
	print("Estado guardado.")

	_exit(0)

def setupPlayersByUserInput():
	global players

	print("Insira o número de jogadores.\n(Atenção, alguns jogos têm um número de jogadores fixo.)")
	playerCount = 0

	while playerCount == 0:
		try: playerCount = int(input("> "))
		except ValueError: print("Número de jogadores inválido.\n")

	players = []
	takenSymbols: list[str] = []

	for i in range(playerCount):
		print(f'Insira o nome do jogador {i + 1}.')
		name = input("> ")

		symbolDone = False
		while not symbolDone:
			print(f'Insira o símbolo do jogador {name} (máx.: 1 caractér).')
			symbol = input("> ")

			try:
				if int(symbol) in range(1, playerCount + 1):
					print("Símbolo não pode ser igual a um número de jogador.")
					continue
			except ValueError: pass

			if len(symbol) > 1:
				symbol = symbol[0]
				print("Símbolo recortado.")

			if symbol in takenSymbols:
				symbol = str(i + 1)
				print("Símbolo duplicado. Será utilizado o número do jogador.")

			players.append(Player(name, symbol, {}, 0))
			takenSymbols.append(symbol)
			symbolDone = True
			print()

def setupPlayersFromSave(saveData: Dict):
	global players

	savePlayers = saveData.get("players")
	for player in savePlayers:
		players.append(
			Player(
				player.get("name"),
				player.get("symbol"),
				player.get("score"),
				player.get("totalScore")
			)
		)

def pickGame():
	global game, players

	print()

	games: list[AbstractController] = [TicTacToe(players), FourInARow(players), Glory(players), Hangman(players)]

	while game is None:
		print("Escolha um dos jogos seguintes.")
		for i in range(len(games)): print(f'{i + 1} - {games[i].title}')

		try:
			gameChoice = int(input("> ")) - 1
			if gameChoice in range(0, len(games)): game = games[gameChoice]
			else: raise ValueError
		except ValueError:
			print("Por favor, apenas selecione um jogo da lista.\n")

# Main code block

def main():
	global game, players

	saveFileExists = exists("save.json")
	saveData: Dict | None = None

	if saveFileExists:
		print("Quer continuar a sessão de jogos anterior? Y/n")
		answer = input("> ").lower()

		print()
		if answer == "y" or answer == "yes" or answer == "sim":
			print("A continuar a prévia sessão de jogos..")
			with open("save.json", "r") as saveFile:
				saveData = loads("".join(saveFile.readlines()))
			setupPlayersFromSave(saveData)
		elif answer == "n" or answer == "no" or answer == "não" or answer == "nao":
			print("A iniciar uma nova sessão de jogos..")
			remove("save.json")
			setupPlayersByUserInput()
		else:
			print("Resposta inválida. O programa irá parar.")
	else:
		setupPlayersByUserInput()

	try:
		while True:
			pickGame()

			if saveData is not None:
				gameData: Dict = saveData.get("gameData")
				gameSaveData: Dict = gameData.get(game.title)
				if gameSaveData is not None:
					print("\nQuer continuar a sessão deste jogo? Y/n")
					answer = input("> ").lower()

					print()
					if answer == "y" or answer == "yes" or answer == "sim":
						print("A continuar da sessão anterior..")
						game.deserialize(gameSaveData.get("controllerData"))
						game.board.deserialize(gameSaveData.get("boardData"))
					else:
						print("A iniciar uma nova sessão..")
						gameData.pop(game.title)
						saveData["gameData"] = gameData
						with open("save.json", "w") as saveFile:
							saveFile.writelines(dumps(saveData, indent=4))

			if listener is None: setupListener()
			winner = game.start()

			print()
			for player in players:
				curScore = player.score.get(game.title)
				if curScore is None: curScore = 0
				player.score[game.title] = curScore

				if player.name == winner.name:
					player.score[game.title] += 1

					totalScore = 0
					for key in player.score.keys(): totalScore += player.score[key]
					player.totalScore = totalScore

				scoreSum = 0
				for key in player.score.keys(): scoreSum += player.score[key]
				print(f'O jogador {player.name} tem {player.score[game.title]} pontos no jogo {game.title}, com {player.totalScore} no total.')

			game = None
	except KeyboardInterrupt:
		save()

if __name__ == "__main__":
	main()