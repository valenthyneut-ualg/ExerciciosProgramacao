if __name__ == "__main__":
    while True:
        euroAmount = input("Escreva uma quantidade de dinheiro em euros (STOP para parar): ")
        if euroAmount == "STOP": break

        try:
            euroAmount = float(euroAmount)
            if euroAmount > 0:
                print(f'{euroAmount}€ em dolares: {(euroAmount * 1.17):.4f}$')
            else: raise ValueError
        except ValueError:
            print("Quantidade inválida! (Este programa apenas aceita números positivos com/sem casas decimais)")