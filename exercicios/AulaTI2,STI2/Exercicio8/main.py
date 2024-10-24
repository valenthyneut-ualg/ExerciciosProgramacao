if __name__ == "__main__":
    values: list[float] = []
    while len(values) < 3:
        try:
            print(f'Valores: {values}')
            values.append(float(input("Digite um número: ")))
        except ValueError:
            print("Valor inválido! (Este programa apenas aceita números com/sem casas decimais)")
        print()
    print(f'Maior valor dos três: {max(values)}')

