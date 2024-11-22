def largestIntIn(num: int):
    strNum = str(num)
    largestNum = strNum[0]
    for char in strNum:
        if int(char) > int(largestNum):
            largestNum = char
    return int(largestNum)

if __name__ == '__main__':
    while True:
        userInput = input("Escreva um número (STOP para parar): ")
        if userInput == 'STOP': break
        try:
            numInput = int(userInput)
            print(f'Maior algarismo no número {numInput}: {largestIntIn(numInput)}')
        except ValueError:
            print("Inseriu um valor inválido (Este programa apenas aceita números inteiros)!")
        print()