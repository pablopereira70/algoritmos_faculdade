def main():
    n = int(input('Digite um número inteiro: '))

    quadrado = 0
    for i in range(1, n):
        temp = i ** 2
        if temp > n:
            break
        quadrado = temp
    
    print(quadrado)


main()