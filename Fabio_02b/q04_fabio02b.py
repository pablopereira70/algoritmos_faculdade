def main():
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a primeira nota: '))
    media = calcular_media(nota_1, nota_2)
    if media >= 7:
        print('APROVADO')
    elif media == 10:
        print('APROVADO COM DISTINÇÃO')
    else:
        print('REPROVADO')


def calcular_media(n1, n2):
    return (n1 + n2) / 2


main()