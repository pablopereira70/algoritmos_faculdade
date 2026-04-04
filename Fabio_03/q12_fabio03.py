def main():
    n = int(input('Digite a quantidade de números: '))
    
    soma = 0
    for i in range(n):
        num = int(input('Digite um número: '))
        soma += num
        
    print('soma = ',soma)
    print('média = ',soma/n)


main()