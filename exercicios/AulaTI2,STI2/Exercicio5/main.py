if __name__ == "__main__":
    while True:
        grade = input("Escreva a nota do aluno, de 0 a 20 (STOP para parar): ")
        if grade == "STOP": break

        try:
            grade = float(grade)
            if grade < 0 or grade > 20: raise ValueError

            if grade >= 9.5:
                print("O aluno passou.")
            else:
                print("O aluno reprovou.")
        except ValueError:
            print("Nota inválida!")