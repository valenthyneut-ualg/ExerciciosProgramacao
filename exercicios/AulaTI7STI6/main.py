from AbstractGame import AbstractController
from Games.TicTacToe.Controller import Controller as TicTacToe
from Games.FourInARow.Controller import Controller as FourInARow
from Games.Glory.Controller import Controller as Glory

if __name__ == "__main__":
    print("Por favor, insira o número de jogadores.")
    print("Atenção, alguns jogos têm um número de jogadores fixo.")

    playerCount = 0
    while playerCount == 0:
        try:
            playerCount = int(input(": "))
        except ValueError:
            print("Número de jogadores inválido!")

    print()

    games: list[type[AbstractController]] = [TicTacToe(), FourInARow(), Glory(playerCount)]
    game = None

    while game is None:
        print("Escolha um jogo dos seguintes:")
        for i in range(len(games)):
            curGame = games[i]
            print(f'{i + 1} - {curGame.gameTitle}')

        try:
            gameChoice = int(input("\n")) - 1
            if gameChoice in range(0, len(games)): game = games[gameChoice]
            else: raise ValueError
        except ValueError: pass

    game.start()