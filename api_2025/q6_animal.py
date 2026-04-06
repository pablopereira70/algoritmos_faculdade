from q4_text_utils import *
from q2_int_utils import *

def main():
    menu = '''
--- APP_ANIMAL ---
[1] para iniciar
[0] para sair
------------------'''

    while True:
        print(menu)
        comando = obter_inteiro_intervalo("--> ", 0, 1)

        if comando == 1:
            ...
        else:
            break


main()