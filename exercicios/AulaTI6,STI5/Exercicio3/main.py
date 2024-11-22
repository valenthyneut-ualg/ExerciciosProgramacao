def smallestIntIn(num: int):
    strNum = str(num)
    smallestNum = strNum[0]
    for char in strNum:
        if int(char) < int(smallestNum):
            smallestNum = char
    return int(smallestNum)

if __name__ == '__main__':
    while True:
        userInput = input("Escreva um número (STOP para parar): ")
        if userInput == 'STOP': break
        try:
            numInput = int(userInput)
            print(f'Menor algarismo no número {numInput}: {smallestIntIn(numInput)}')
        except ValueError:
            print("Inseriu um valor inválido (Este programa apenas aceita números inteiros)!")
        print()