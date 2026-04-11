from utils import *

def main():
    menu = '''
--- APP_ATIVIDADE_FÍSICA ---
[1] para iniciar
[0] para sair
----------------------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo(0, 1)

        if comando == 1:
            ...
        else:
            break

main()