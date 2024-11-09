if __name__ == "__main__":
    values: list[int] = []
    parityCount: [int] = [0, 0]

    i = 0
    while i < 10:
        try:
            value = int(input("Escreva um número: "))
            values.append(value)
            if value % 2 == 0: parityCount[0] += 1
            else: parityCount[1] += 1
            i += 1
        except ValueError:
            print("Inseriu um valor inválido! (este programa apenas aceita números inteiros)")

    print()
    print(f'Valores que inseriu: {", ".join(str(x) for x in values)}')
    print(f'Diferença entre o maior e o menor valor: {max(values) - min(values)}')
    print(f'Nº de números pares: {parityCount[0]}; Nº de números impares: {parityCount[1]}')