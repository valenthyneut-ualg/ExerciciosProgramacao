# Algoritmo:
#
# Geramos três valores aleatórios, o primeiro sendo entre 0 e 10,
# o segundo e terceiro entre 5 e 20.
#
# Utilizando estes valores como a, b, c respetivamente, calculamos
# a fórmula resolvente, começando com o discriminante (b^2 - 4ac).
#
# Se o discriminante for inferior a 0, mostramos ao utilizador que
# não existem raízes reais.
# Senão, continuamos com os cálculos. Calculamos a raiz do
# discriminante e realizamos dois cálculos da fórmula: O positivo
# e o negativo. Ou seja,  -b +- discriminante / 2 * a
#
# No final, mostramos o resultado ao utilizador.
#
# (No caso deste programa em específico, repetimos estes passos 5
# vezes como forma de teste.)

from math import sqrt
from random import randrange

def quadraticFormula(a: float, b: float, c: float) -> str:
    if a == 0: return "Não é possível calcular com um denominador igual a 0."
    discriminant = ((b ** 2) - (4 * a * c))
    if discriminant < 0:
        return "Não existem raízes reais."
    discriminant = sqrt(discriminant)
    sumResult = (-b + discriminant) / (2 * a)
    subResult = (-b - discriminant) / (2 * a)
    return f'{sumResult:.2f}, {subResult:.2f}'

for i in range(0, 5):
    a = randrange(0, 10)
    b = randrange(5, 20)
    c = randrange(5, 20)
    print(f'a: {a}; b: {b}; c: {c};')
    print(quadraticFormula(a, b, c))
    print()