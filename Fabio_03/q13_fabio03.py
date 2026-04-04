def main():
    n = int(input('Digite a quantidade de números: '))
    
    maior = 0
    for i in range(n):
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
    
    print(maior)


main()