if __name__ == "__main__":
    while True:
        try:
            factorialNum = input("Escreva um número (STOP para parar): ")
            if factorialNum == "STOP": exit()

            factorialNum = int(factorialNum)

            factorial = 1
            factorialStr = ""

            for i in reversed(range(1, factorialNum + 1)):
                factorial *= i
                factorialStr += str(i)
                if i > 1: factorialStr += " * "

            print(f'{factorialStr} = {factorial}')
            print()

            # math.factorial also exists but that's boring
        except ValueError:
            print("Valor inválido! (Este programa apenas aceita números inteiros (sem casas decimais)")