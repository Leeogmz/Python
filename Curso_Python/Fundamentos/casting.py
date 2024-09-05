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