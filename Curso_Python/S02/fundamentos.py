#Comentários

# isto é um comentário
# isto é um comentário

print('Hello, word!') # isto é um comentário


''' Este é um comentario
o comentario continua aqui 
aqui ainda continua
e aqui termina '''

#Metodo Print

print('Olá, mundo!')
print(10)
print(20.5)

print('Maça', 20, 30.45)

print('Maça', 'Pera', 'Uva', sep=' - ')

print('Maça', 'Pera', end=' Fim', sep=' ')

print('Este é um texto longo, \n e eu quero quebrar a linha')

print('Maça', 'Pera', 'Uva', sep='\n')

print('A pontuação total de %s foi %s pontos' % ('Fernando', '10'))

print('A pontuação total de {} foi {} pontos'.format('Fernando', '10'))

#Variaveis

_numero = 1
Numero = 2
numero = 3
numero123 = 4

print(_numero, Numero, numero, numero123)

numero = 10 
print(numero)
numero = 20 
print(numero)

texto = 'Olá mundo!'

print(texto)

#Tipos primitivos

variavel = None

print(variavel)

inteiro = 10
print(inteiro)

decimal = 1.53
print(decimal)

texto = 'Olá, isso é um texto'
print(texto)

var = True
print(var)
var = False
print(var)

var1 = 10 
var2= var1
print(var2)

var = None
print(var)
var = 1
print(var)
var = 'texto'
print(var)

saldoBancario = 100 #Camel Case
SaldoBancario = 100 #Pascal Case
saldo_bancario = 100 #snake case

#Formatação

# %s texto
# %d inteiro
# %f real

nome = 'Ana'
texto_formatado = 'O nome dela é %s' % (nome)
print(texto_formatado)

nome = 'Rodrigo'
idade = 23
altura = 1.73

texto = 'Meu nome é %s, tenho %d anos, e tenho %f metros de altura' % (nome, idade, altura)
print(texto)

numero_gigante =  1.123456789
print('Numero gigante formatado: %.2f' % (numero_gigante))

valor = True

print('O valor é: %s' % (valor))
print('O valor é %d' % (valor))

decimal = 23.456
print('A parte inteira é %d' % (decimal))

texto = 'Olá, assim se quebra uma linha, \n\tentendeu como quebra a linhda? \n\t\tfim'
print(texto)

texto = 'Deixa a \'palavra\' entre as aspas'
print(texto)
