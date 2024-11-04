if __name__ == "__main__":
    people: list[(str, str, int)] = []
    while True:
        try:
            name = input("Escreva o nome do indivíduo: ")

            idNum = input(f'Escreva o número de cartão de cidadão de {name}: ')
            if len(idNum) != 8 or not idNum.isnumeric(): raise ValueError

            age = int(input(f'Escreva a idade de {name} em anos (insira 999 para parar): '))
            if age < 0: raise ValueError
            if age == 999: break

            people.append((name, idNum, age))
            print()
        except ValueError:
            print("Inseriu um valor inválido!")
            print("O número do cartão de cidadão tem de ter apenas 8 digitos.")
            print("A idade tem de ser maior que 0, e só pode ser um número inteiro.")
            print()

    print()
    if len(people) == 0:
        print("Não inseriu pessoas nenhumas.")
    else:
        youngestPerson = people[0]
        for person in people:
            if person[2] < youngestPerson[2]:
                youngestPerson = person
        print(f'Pessoa mais nova de {len(people)} pessoas:')
        print(f'{youngestPerson[0]}, com Nº CC {youngestPerson[1]}, {youngestPerson[2]} anos de idade')