if __name__ == "__main__":
    while True:
        try:
            minimum = input("Escreva um número para utilizar como mínimo (STOP para parar): ")
            if minimum == "STOP": exit()

            minimum = int(minimum)
            maximum = int(input("Escreva um número para utilizar como máximo: "))

            total = 0
            sumStr = ""

            for i in range(minimum, maximum + 1):
                total += i
                sumStr += str(i)
                if i < maximum: sumStr += " + "

            print(f'{sumStr} = {total}')
            print()
        except ValueError:
            print("Valor inválido! (Este programa apenas aceita números inteiros (sem casas decimais)")