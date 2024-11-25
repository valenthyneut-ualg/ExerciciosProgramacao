def readUnitName() -> str:
    unitName = input("Escreva o nome da unidade curricular: ")
    splitUnitName = unitName.split(" ")
    unitInitials = ""
    for word in splitUnitName:
        unitInitials += word[0].upper()
    return readUnitGrade(unitInitials)

def readUnitGrade(unitInitials: str) -> str:
    try:
        unitGrade = int(input("Escreva a nota esperada da unidade curricular: "))
        return f'{unitInitials} - {unitGrade}'
    except ValueError:
        readUnitGrade(unitInitials)

if __name__ == "__main__":
    while True:
        print(readUnitName())
        print()