# Input

valor_escrito = input()
print(type(valor_escrito))
print(valor_escrito)

meu_nome = input()
print('Eu me chamo %s' % (meu_nome))

dia = input('Insira o dia: ') 
mes = input('Insira o mes: ')
ano = input('Insira o ano: ')
print('A data inserida foi %s/%s/%s' % (dia, mes,ano))

entrada_usuario = input('Digite 1 para verdadeiro e 0 para Falso: ')
valor_inteiro = int(entrada_usuario)
valor_logico = bool(valor_inteiro)
print('Você escolheu: %s' % (valor_logico))
print('Ou ainda você escolheu: %d' % (valor_inteiro))