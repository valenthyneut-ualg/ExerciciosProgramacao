from Games.TicTacToe.Controller import Controller as TicTacToe
from Games.Glory.Controller import Controller as Glory
from Games.AbstractController import AbstractController

if __name__ == "__main__":
	controllers: tuple[AbstractController | None] = (TicTacToe(), None, Glory(2))
	controller = None

	while controller == None:
		print("Escolha um jogo dos seguintes três:")
		print("1 - Jogo do Galo")
		print("2 - 4 em linha")
		print("3 - Jogo da Glória")

		try:
			gameChoice = int(input("\n")) - 1
			if gameChoice in range(0, 3): controller = controllers[gameChoice]
			else: raise ValueError("\nJogo inválido.\n")
		except ValueError as error:
			print(error)

	if isinstance(controller, AbstractController): controller.start()