from FourInARow.Board import Board

if __name__ == "__main__":
    board = Board()
    turn = True
    lastPlayedCoords: tuple[int, int] = (1, 1)

    print("Insira o número onde quer colocar a sua peça.")
    print("(QUIT para parar)")

    while True:
        turnPlayer = "X" if turn else "O"
        print()
        board.display()

        inWinState, player = board.inWinState(lastPlayedCoords)

        if inWinState:
            print()
            print(f'O jogador [{player}] ganhou!')
            break

        gameInput = input(f'[{turnPlayer}] > ')
        if gameInput == "QUIT": exit()

        try:
            column = int(gameInput)
            if column not in range(1, 9): raise ValueError("O número da coluna tem de estar compreendido entre 1 e 8! (inclusivo)")

            lastPlayedCoords = board.play(turnPlayer, column)
            turn = not turn
        except ValueError as exception:
            print("Inseriu uma posição inválida!")
            print(exception)