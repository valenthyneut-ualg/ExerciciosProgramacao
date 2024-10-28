from math import sqrt

def parsePoint(rawPoint: str) -> [float, float]:
    rawPoint.index(",")
    rawPointCoords = rawPoint.split(",")
    pointCoords = []
    for point in rawPointCoords:
        pointCoords.append(float(point.strip()))
    return pointCoords

def distanceBetweenPoints(point1: [float, float], point2: [float, float]) -> float:
    xResult = (point2[0] - point1[0]) ** 2
    yResult = (point2[1] - point1[1]) ** 2
    xySum = xResult + yResult
    return sqrt(abs(xySum))

if __name__ == '__main__':
    while True:
        try:
            p1 = input("Escreva dois números inteiros separados por vírgula\n(Exemplo: '19,12'; STOP para parar): ")

            if p1 == "STOP": break
            p1 = parsePoint(p1)

            p2 = parsePoint(input("Escreva mais dois números inteiros separados por vírgula\n(Exemplo: '3,15'): "))

            print(f'A distância entre {p1} e {p2} é ~{distanceBetweenPoints(p1, p2):.2f} unidades.')
            print()
        except ValueError:
            print("Ponto inválido! (Este programa apenas aceita números decimais, no formato especificado.")