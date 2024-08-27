#1°

primeiro_numero = float(input('Por favor, digite o primeiro numero: '))
segundo_numero = float(input('Por favor, digite o segundo numero: '))
divisao = primeiro_numero / segundo_numero
print(" %.2f dividido por %.2f é igual a: %.2f." % (primeiro_numero, segundo_numero, divisao))

#2°

dia = input('Digite o dia: ')
mes = input('Digite o mês: ')
ano = input('Digite o ano: ')
hora = input('Digite a hora: ')
minuto = input('Digite o minuto: ')
segundos = input('Digite os segundos: ')

print('%s/%s/%s  %s:%s:%s' % (dia, mes, ano, hora, minuto, segundos))