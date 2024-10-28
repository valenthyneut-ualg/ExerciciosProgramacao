if __name__ == '__main__':
    while True:
        try:
            num = input("Escreva um número (STOP para parar): ")
            if num == "STOP": exit()

            num = float(num)
            for i in range(1, 11):
                print(f'{num} * {i} = {num * i}')
            print()
        except ValueError:
            print("Valor inválido! (Este programa apenas aceita números com/sem casas decimais)")