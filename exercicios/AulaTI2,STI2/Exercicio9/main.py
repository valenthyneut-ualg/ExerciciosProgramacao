students: dict[str, (float, float)] = {}

if __name__ == "__main__":
    while True:
        name = input("Escreva o nome de um aluno (STOP para parar e ver os resultados): ")
        if name == "STOP": break

        try:
            if len(name.strip()) < 0: raise ValueError

            height = float(input(f'Escreva a altura do aluno "{name}", em metros: '))
            age = float(input(f'Escreva a idade do aluno "{name}": '))
            students[name] = (height, age)
        except ValueError:
            print("""
                Introduziu um valor inválido!\n
                (O campo "Nome" tem de ter pelo menos 1 caracter; Os campos Idade e Altura têm de ser números positivos com/sem casas decimais)
                """)
        print()
    if len(students) == 0:
        print("Não introduziu dados nenhums.")
    else:
        # next(iter(dict.keys())): Get the first value of the dictionary
        tallestStudent = next(iter(students.keys()))
        youngestStudent = next(iter(students.keys()))

        for studentName in students:
            curStudentData = students[studentName]
            if curStudentData[0] > students[tallestStudent][0]: tallestStudent = studentName
            if curStudentData[1] < students[youngestStudent][1]: youngestStudent = studentName
            # This part is a bit convoluted, but I like neat data types that make it "easy" to store data.
            # What's happening here is that the students Dictionary holds a tuple, it's first index being
            # the height, and the second being the age. Both "tallestStudent" and "youngestStudent" are a
            # string, which is the data type of the "student"'s Dictionary keys.

        print(f'Aluno mais alto: {tallestStudent}, com a altura: {students[tallestStudent][0]}m')
        print(f'Aluno mais novo: {youngestStudent}, com a idade: {students[youngestStudent][1]}')