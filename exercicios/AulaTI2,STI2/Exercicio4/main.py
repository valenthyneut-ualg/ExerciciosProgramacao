from math import pi

if __name__ == "__main__":
    while True:
        radius = input("Escreva o raio do círculo (STOP para parar): ")
        if radius == "STOP": break

        try:
            radius = float(radius)
            if radius <= 0: raise ValueError

            perimeter = 2 * pi * radius
            area = pi * radius ** 2
            print(f'Perímetro: {perimeter}; Área do círculo: {area};')
        except ValueError:
            print("Raio inválido! (Este programa apenas aceita números positivos com/sem casas decimais)")