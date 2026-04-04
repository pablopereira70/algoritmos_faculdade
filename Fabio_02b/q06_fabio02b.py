def main():
    painel_de_selecao()
    turno = input()
    if turno == "M":
        print('Bom dia!')
    elif turno == "V":
        print('Boa tarde!')
    elif turno == 'N':
        print('Boa noite!')
    else:
        print('Valor inválido')


def painel_de_selecao():
    print('''
   ESCREVA
[M] matutino
[V] vespertino
[N] noturno''')
    

main()