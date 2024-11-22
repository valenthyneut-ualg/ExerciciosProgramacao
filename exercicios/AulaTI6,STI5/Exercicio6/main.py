def valueInList(value, searchList: list):
    for item in searchList:
        if item == value: return True
    return False

def readIntoList() -> list:
    valueList = []
    while True:
        userInput = input("Escreva um valor (NEXT para prosseguir): ")
        if userInput == "NEXT": break
        valueList.append(userInput)
    return valueList

if __name__ == "__main__":
    userList = readIntoList()
    print()
    searchValue = input("Escreva um valor para procurar na lista: ")
    print(f'O valor {"não " if not valueInList(searchValue, userList) else ""}está na lista.')