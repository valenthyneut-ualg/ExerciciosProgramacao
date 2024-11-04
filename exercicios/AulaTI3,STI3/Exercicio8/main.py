def factors(n: int):
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                yield i
                break

if __name__ == "__main__":
    while True:
        try:
            num = input("Escreva um número para decompor em fatores primos (STOP para parar): ")
            if num == "STOP": exit()

            num = int(num)
            if num <= 0: raise ValueError
            if num == 1:
                print("1 não tem fatores primos.")
            else:
                numFactors = factors(num)
                factorsString = f'{num} = {' * '.join(str(x) for x in factors(num))}'
                print(factorsString)
        except ValueError:
            print("Inseriu um valor inválido (Este programa só aceita números inteiros positivos)")