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

#Operadores aritmeticos 

print ( 10 + 20)

numero = 10 + 10.5
print(numero)

outro_numero = 30 + numero
print(outro_numero)

numero = 20 - 10 
print(numero)

numero = 10 * 2 
print(numero)

numero = 10 / 3
print(numero)

numero = 10 // 3 # Para trazer apenas a parte inteira
print(numero)

numero = 2 ** 4 #Exponenciação
print(numero)

numero =  4 % 3 #Resto da divião
print(numero)

nume1 = 10 * 2 + 1
print(nume1)

nume1 = 10 * (2 + 1)
print(nume1)

nume1 = 3 * 3 - 9
print(nume1)

nume1 = 3 * (3 - 9)
print(nume1)

nume1 = 20
nume2 = 40
nume3 = 60
resultado = nume1 + nume2 + nume3
print(resultado)

resultado = resultado * 2
print(resultado)

a = 1
a += 1
print (a)

#Operadores Logicos

resultado1 = True and False
print(resultado1)

resultado2 = True and True
print(resultado2)

var1 = True
var2 = False
var3 = False
print(var1 and var2 and var3)

clima_bom = True
estou_disposto = False
vou_ao_mercado = clima_bom and estou_disposto
print('Vou ao mercado? ' , vou_ao_mercado)

result1 = True or False
print(result1)

result1 = False or False
print(result1)

sei_programar = True
sei_investir = False
ganho_bom_salario = sei_programar or sei_investir
print('Terei um bom salario? ', ganho_bom_salario)

result2 = False
print(not result2)

porta_aberta = False
tem_chave = False
print('Estou trancado? ', not porta_aberta and not tem_chave)

# prioridade 
# NOT, AND, OR

bool1 = True or False and True
print(bool1)

bool2 = True or not False
print(bool2)

bool3 = True and not (True or False)
print(bool3)

#Casting

texto = 'Olá'
numero = 2
decimal = 1.5
booleano = True
print(type(texto))
print(type(numero))
print(type(decimal))
print(type(booleano))

texto1 = '2'
texto2 = '1.5'
num1 = int(texto1)
num2 = float(texto2)

print(type(texto1))
print(type(texto2))
print(type(num1))
print(type(num2))

num = 21.45646
inteiro = int(num)
print(inteiro)

texto = "O numero é "
numero = 10.3
numero_em_string = str(numero)
print(texto, numero_em_string)
print(type(numero_em_string))

numero = 123
texto = str(numero)
numero_de_digitos = len(texto)
print(numero_de_digitos)


vazio = None
numero_um = 15
numero_zero = 0
texto ='Texto'
texto_vazio = ""
decimal_zero = 0.0
decimal = 3.5

print('Variavel tem valor: ', bool(vazio))

print('Numero tem valor: ', bool(numero_um))
print('Numero tem valor: ', bool(numero_zero))

print('String tem conteudo: ', bool(texto))
print('String tem conteudo: ', bool(texto_vazio))

print('Float tem valor: ', bool(decimal_zero))
print('Float tem valor: ', bool(decimal))

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

#Operadores de Atribuição e combinação de operadores lógicos

numero = 1
#numero = numero +1
numero += 1
print('Numero é: ', numero)

numero = 10
#numero = numero /2
numero /= 2
print('Numero dividido é: ', numero)

num = 20
booleana = (num == 10)
print(booleana)

num = 20
booleana = (num != 10)
print(booleana)

num1 = 10
num2 = 20
e_maior = num1 > num2
print(e_maior)

num1 = 10
num2 = 20
e_maior = num1 <= num2
print(e_maior)

num = 5
boolean = num > 0 and num < 10
print(boolean)

num = 10.1
boolean = type(num) == float and (num == 10.1 or num == 20.2)
print(boolean)

#Slicing

var = "Exemplo"
print(var[1:3])
print(var[3:])
print(var[:5])