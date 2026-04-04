def main():
    senha_usuario = input('Digite a senha: ')
    
    senha = '1234'
    if senha_usuario == senha:
        print('Acesso concedido')
    else:
        print('Acesso negado')


main()