#entrada
min_totais = int(input('Digite um valor(minutos): '))
#processamento
hora_temp = min_totais // 60
dia = hora_temp // 24
hora = hora_temp % 24
min = min_totais % 60
#saída
print(f'{min_totais} minutos equivalem a {dia} dias, {hora} horas e {min} minutos')