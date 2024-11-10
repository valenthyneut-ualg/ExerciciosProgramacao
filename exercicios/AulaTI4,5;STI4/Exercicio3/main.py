def indexOfInt(searchValue: int, searchList: list[int]) -> int:
    for i in range(len(searchList)):
        if searchValue == searchList[i]:
            return i
    return -1

if __name__ == "__main__":
    values: list[int] = []
    searchValue: int | None = None
    while True:
        try:
            if len(values) > 0: print(f'Valores inseridos: {", ".join(str(x) for x in values)}')
            value = input("Escreva um número (STOP para pesquisar): ")
            if value == "STOP": break

            values.append(int(value))
            print()
        except ValueError:
            print("Inseriu um valor errado! (Este programa apenas aceita números inteiros)")
    while searchValue is None:
        try:
            searchValue = int(input("Escreva um número para pesquisar na lista: "))
        except ValueError:
            print("Inseriu um valor errado! (Este programa apenas aceita números inteiros)")

    searchResult = indexOfInt(searchValue, values)
    if searchResult == -1:
        print("O valor não foi encontrado na lista.")
    else:
        print(f'Índice do valor na lista: {searchResult}')

