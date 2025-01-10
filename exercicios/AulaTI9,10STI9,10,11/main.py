import os
from json import loads, dumps
from os import remove
from os.path import exists
from typing import Dict
from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from Games.TicTacToe.Controller import Controller as TicTacToe
from Games.FourInARow.Controller import Controller as FourInARow
from Games.Glory.Controller import Controller as Glory
from Games.Hangman.Controller import Controller as Hangman
from pynput.keyboard import GlobalHotKeys, Listener

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
					if title != game.title:
						gameData[title] = existingGameData.get(title)

	saveData = dumps({
		"players": playerData,
		"gameData": gameData
	}, indent=4)

	with open("save.json", "w") as saveFile: saveFile.writelines(saveData)
	print("Jogo guardado.")

	os._exit(0)

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

			players.append(Player(name, symbol))
			takenSymbols.append(symbol)
			symbolDone = True
			print()

def setupPlayersFromSave(saveData: Dict):
	global players

	savePlayers = saveData.get("players")
	for player in savePlayers:
		players.append(Player(player.get("name"), player.get("symbol")))

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
			print("A continuar a prévia sessão de jogos..\n")
			with open("save.json", "r") as saveFile:
				saveData = loads("".join(saveFile.readlines()))
			setupPlayersFromSave(saveData)
		elif answer == "n" or answer == "no" or answer == "não" or answer == "nao":
			print("A iniciar uma nova sessão de jogos..\n")
			remove("save.json")
			setupPlayersByUserInput()
		else:
			print("Resposta inválida. O programa irá parar.")
	else:
		setupPlayersByUserInput()

	pickGame()

	if saveData is not None:
		gameSaveData: Dict = saveData.get("gameData").get(game.title)
		if gameSaveData is not None:
			print("Quer continuar a sessão deste jogo? Y/n")
			answer = input("> ").lower()

			print()
			if answer == "y" or answer == "yes" or answer == "sim":
				print("A continuar da sessão anterior..\n")
				game.deserialize(gameSaveData.get("controllerData"))
				game.board.deserialize(gameSaveData.get("boardData"))
			else:
				print("A iniciar uma nova sessão..\n")

	setupListener()
	game.start()

if __name__ == "__main__":
	main()