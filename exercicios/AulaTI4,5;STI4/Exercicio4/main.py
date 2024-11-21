# Algoritmo do jogo:
#
# Num loop:
#   Mostrar o estado do jogo (apresentar o quadro)
#   Verificar o estado do jogo,
#   se sim:
#       parar o jogo, dizer qual o jogador que ganhou (ou se foi um empate)
#   se não:
#       deixar o respetivo jogador colocar o seu símbolo no quadro
#       alternar o turno dos jogadores
#       repetir

from TicTacToe.Board import Board

if __name__ == "__main__":
    board = Board()
    turn = True


    print("Insira um par de coordenadas separado por vírgula onde:")
    print("O primeiro número é a linha e o segundo a coluna.")
    print("Exemplo: 2, 3")
    print("(QUIT para parar)")

    while True:
        turnPlayer = "X" if turn else "O"
        print()
        board.display()

        inWinState, player = board.inWinState()
        if inWinState:
            print(f'\nO jogador [{player}] ganhou!')
            break

        # Check if there are no whitespaces left, meaning we have a draw.
        if board.state.count(" ") == 0:
            print("\nEmpate!")
            break

        print()

        gameInput = input(f'[{turnPlayer}] > ')
        if gameInput == "QUIT": exit()

        try:
            coordinates = [int(n) for n in gameInput.split(",")]
            if len(coordinates) != 2:
                raise ValueError("Apenas pode inserir dois pontos na coordenada!")

            if coordinates[0] not in range(1, 4) or coordinates[1] not in range(1, 4):
                raise ValueError("Os números das coordenadas têm de estar compreendidas entre 1 e 3! (inclusivo)")

            board.play(turnPlayer, coordinates[0], coordinates[1])
            turn = not turn
        except ValueError as exception:
            print(f'Inseriu uma posição inválida!\n{exception}')