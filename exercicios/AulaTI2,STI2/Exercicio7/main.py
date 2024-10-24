possibleStates = ["Nenhum", "Ligar", "Desligar", "Furar"]

if __name__ == "__main__":
    state = possibleStates[0]
    while True:

        print(f'Estado atual da máquina: {state}')
        print()

        userInput = input("Insira uma letra para alterar o estado da máquina (L, D ou F. STOP para parar): ")
        if userInput == "STOP": break

        if userInput == "L":
            state = possibleStates[1]
        elif userInput == "D":
            state = possibleStates[2]
        elif userInput == "F":
            state = possibleStates[3]
        else: print("Estado inválido! (Escreva um de L, D ou F.")