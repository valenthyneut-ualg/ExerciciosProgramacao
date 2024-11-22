def sort(intList: list[int]) -> list[int]:
    for i in range(1, len(intList)):
        key = intList[i]
        prev = i - 1

        while prev >= 0 and key < intList[prev]:
            intList[prev + 1] = intList[prev]
            prev -= 1
        intList[prev + 1] = key
    return intList

def readIntoList() -> list[int]:
    intList: list[int] = []
    while True:
        try:
            userInput = input("Escreva um número inteiro (STOP para parar): ")
            if userInput == "STOP": break

            intList.append(int(userInput))
        except ValueError:
            print("Inseriu um valor inválido!")
    return intList

if __name__ == '__main__':
    userList = readIntoList()
    print(f'Lista não ordenada: {userList}')
    print(f'Lista ordenada: {sort(userList)}')