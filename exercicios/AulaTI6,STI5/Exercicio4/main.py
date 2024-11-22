def readIntoList() -> list[int]:
    intList: list[int] = []
    while len(intList) < 10:
        try: intList.append(int(input("Escreva um número inteiro: ")))
        except ValueError: print("Inseriu um valor inválido!")
    return intList

def maxMinDifference(intList: list[int]) -> tuple[int, int, int]:
    maxInt = max(intList)
    minInt = min(intList)
    return maxInt - minInt, maxInt, minInt

def evenUnevenCount(intList: list[int]) -> tuple[int, int]:
    evenCount = 0
    unevenCount = 0
    for i in intList:
        if i % 2 == 0: evenCount += 1
        else: unevenCount += 1
    return evenCount, unevenCount

if __name__ == "__main__":
    userIntList = readIntoList()

    difference, maxUserInt, minUserInt = maxMinDifference(userIntList)
    print(f'Diferença entre o maior ({maxUserInt}) e menor ({minUserInt}) valor da lista: {difference}')

    userEvenCount, userUnevenCount = evenUnevenCount(userIntList)
    print(f'Nº de números pares: {userEvenCount}; Nº de números ímpares: {userUnevenCount}.')
