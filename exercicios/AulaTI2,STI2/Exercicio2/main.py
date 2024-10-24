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