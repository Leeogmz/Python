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