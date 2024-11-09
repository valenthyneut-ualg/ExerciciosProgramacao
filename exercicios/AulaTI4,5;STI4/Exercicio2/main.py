if __name__ == "__main__":
    values: list[int] = []

    while True:
        try:
            value = input("Escreva um valor (STOP para ordenar): ")
            if value == "STOP": break

            value = int(value)
            values.append(value)
        except ValueError:
            print("Inseriu um valor errado! (Este programa apenas aceita números inteiros.)")

    if len(values) <= 0:
        print("Não inseriu nenhums valores.")
    else:
        values.sort()
        print(f'Lista ordenada: {", ".join(str(x) for x in values)}')