if __name__ == "__main__":
    while True:
        height = input("Escreva a altura de um rétangulo (STOP para parar): ")
        if height == "STOP": break

        try:
            height = float(height)
            width = float(input("Escreva a largura desse rétangulo: "))
            if width <= 0 or height <= 0: raise ValueError

            if height == width:
                print("O seu rétangulo é um quadrado!")
            else:
                print("O seu rétangulo náo é um quadrado!")

            area = height * width
            print(f'Área: {area}')
        except ValueError:
            print("Inseriu um valor inválido! (Este programa apenas aceita números positivos com/sem casas decimais)")
        print()