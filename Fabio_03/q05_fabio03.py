def main():
    numero = int(input('Digite um número inteiro: '))

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i

    print(fatorial) 


main()