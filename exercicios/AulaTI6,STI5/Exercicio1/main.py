def powerOf(num: float, exponent: float):
    return num ** exponent

if __name__ == '__main__':
    while True:
        userInput = input("Escreva um número (STOP para parar): ")
        if userInput == 'STOP': break
        try:
            numInput = float(userInput)
            exponentInput = float(input("Escreva um expoente: "))
            print(f'{numInput} elevado a {exponentInput} = {powerOf(numInput, exponentInput)}')
        except ValueError:
            print("Inseriu um valor inválido (Este programa apenas aceita números)!")
        print()