def readName() -> str:
    name = input("Escreva o seu nome completo: ")
    splitName = name.split(" ")
    if len(splitName) <= 1:
        return name
    else:
        lastName = splitName[-1]
        lastName += ", "
        return lastName + " ".join(splitName[0:len(splitName) - 1])

if __name__ == "__main__":
    print(readName())