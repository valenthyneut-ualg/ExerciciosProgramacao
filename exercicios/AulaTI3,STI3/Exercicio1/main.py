def isPrime(number: int) -> bool:
    if number < 2: return False
    for i in range(2, number):
        if number % i == 0: return False
    return True

if __name__ == '__main__':
    while True:
        try:
            number = input("Escreva um número inteiro positivo (STOP para parar): ")
            if number == "STOP": break

            number = int(number)
            print(f'{number} é primo.' if isPrime(number) else f'{number} não é primo.')
        except ValueError:
            print("Número inválido! (Este programa apenas aceita números inteiros positivos)")