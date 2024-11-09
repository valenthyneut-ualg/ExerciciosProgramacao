if __name__ == "__main__":
    # This is an unbelievably stupid way of
    # saving information but the exercise
    # demands it.

    youngestAge: int | None = None
    youngestAgeClass: str | None = None

    oldestAge: int | None = None
    oldestAgeClass: str | None = None

    girlCount: int | None = 0

    highestGrade: int | None = None
    highestGradeClass: str | None = None
    highestGradeGender: str | None = None

    while True:
        try:
            className = input("Escreva a turma do aluno (STOP para parar): ")
            if className == "STOP": exit()

            age = int(input("Escreva a idade do aluno: "))
            if age < 0: raise ValueError

            gender = int(input("Escreva o género do aluno (masculino - 1, feminino - 0): "))
            if gender == 0:
                gender = "Feminino"
            elif gender == 1:
                gender = "Masculino"
            else: raise ValueError

            grade = int(input("Escreva a nota do aluno: "))
            if grade < 0 or grade > 20: raise ValueError

            if youngestAge is None or age < youngestAge:
                youngestAge = age
                youngestAgeClass = className

            if oldestAge is None or age > oldestAge:
                oldestAge = age
                oldestAgeClass = className

            if gender == "Feminino":
                girlCount += 1

            if highestGrade is None or highestGrade < grade:
                highestGrade = grade
                highestGradeClass = className
                highestGradeGender = gender

            print()
            print(f'Turma com o aluno mais novo: {youngestAgeClass}; Idade: {youngestAge};')
            print(f'Turma com o aluno mais velho: {oldestAgeClass}; Idade: {oldestAge};')
            print(f'Nº de raparigas no TeSP-DEE: {girlCount}')
            print(f'Turma com a nota mais alta: {highestGradeClass}; Nota: {highestGrade}; Género do aluno: {highestGradeGender}')
            print()
        except ValueError:
            print("Inseriu um valor inválido!")
            print("O campo 'idade' tem de ser um número inteiro superior a 0.")
            print("O campo 'género' tem de ser um dos próximos valores: 1, 0.")
            print("O campo 'nota' tem de ser um número superior ou igual a 0 e inferior ou igual a 20.")