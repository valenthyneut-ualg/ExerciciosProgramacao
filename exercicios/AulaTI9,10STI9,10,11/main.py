from AbstractGame.Player import Player
from AbstractGame.AbstractController import AbstractController

from Games.TicTacToe.Controller import Controller as TicTacToe
from Games.FourInARow.Controller import Controller as FourInARow
from Games.Glory.Controller import Controller as Glory
from Games.Hangman.Controller import Controller as Hangman

if __name__ == "__main__":
	print("Insira o número de jogadores.")
	print("(Atenção, alguns jogos têm um número de jogadores fixo.)")

	playerCount = 0
	while playerCount == 0:
		try: playerCount = int(input("> "))
		except ValueError: print("Número de jogadores inválido!")

	print()

	players: list[Player] = []
	takenSymbols: list[str] = []

	for i in range(playerCount):
		print(f'Insira o nome do jogador {i + 1}.')
		name = input("> ")

		print("Insira o símbolo do jogador (máx.: 1 caractér).")
		symbol = input("> ")
		if len(symbol) > 1:
			symbol = symbol[0]
			print("Símbolo recortado por ser demasiado longo.")

		if symbol in takenSymbols:
			symbol = str(i + 1)
			print("Símbolo duplicado. Será utilizado o número do jogador.")

		players.append(Player(name, symbol))
		takenSymbols.append(symbol)
		print()

	games = [TicTacToe(players), FourInARow(players), Glory(players), Hangman()]
	game: AbstractController | None = None

	while game is None:
		print("Escolha um jogo dos seguintes.")
		for i in range(len(games)): print(f'{i + 1} - {games[i].title}')

		try:
			gameChoice = int(input("> ")) - 1
			if gameChoice in range(0, len(games)): game = games[gameChoice]
			else: raise ValueError
		except ValueError:
			print("Só pode selecionar um jogo da lista!")

	print()
	game.start()