from functools import reduce

disciplines = ["Matemática", "Português", "Inglês", "Geografia"]

if __name__ == '__main__':
    grades = []
    curDiscipline = 0

    while curDiscipline < len(disciplines):
        try:
            grade = input(f'Escreva uma nota para a disciplina de {disciplines[curDiscipline]} (STOP para parar): ')
            if grade == 'STOP': exit()

            grade = float(grade)
            if grade < 0 or grade > 20: raise ValueError

            grades.append(grade)
            curDiscipline += 1
        except ValueError:
            print("Valor inválido! (Este programa apenas aceita números positivos entre 0 a 20 com/sem casas decimais.)")

    finalAverage = reduce(lambda accumulator, value: accumulator + value, grades, 0) / len(grades)
    # This line is equal to the following:
    #
    # sum = 0
    # for grade in grades: sum += grade
    # sum /= len(grades)

    print()
    print(f'Nota final: {finalAverage} pontos.')
    print("Aprovado." if finalAverage >= 9.5 else "Reprovado.")