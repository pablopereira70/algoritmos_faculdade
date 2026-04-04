#entrada
numero = int(input('Digite um número inteiro de três algarismos:'))
#processamento
algarismo_1 = numero // 100
algarismo_2 = (numero % 100) // 10
algarismo_3 = (numero % 100) % 10
#saída
print(f'O número {numero} em ordem inversa é igual a {algarismo_3}{algarismo_2}{algarismo_1}')