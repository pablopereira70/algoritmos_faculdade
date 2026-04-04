#entrada
dia_total = int(input('Digite a sua idade(dias): '))
#processamento
anos = dia_total // 365
mes = (dia_total % 365) // 30
dia_parcial = (dia_total % 365) % 30
#saída
print(f'A sua idade corresponde a {anos} anos, {mes} meses e {dia_parcial} dias')