num1 = -10
num2 = 10
print(abs(num1))
print(abs(num2))
print(abs(num1) + abs(num2))

maior_valor = max(10,20,30)
print(maior_valor)

lista = [-20, 1,2.3,3]
print(max(lista))
print(min(lista))

x = 2
y = 3
print(2**3)
print(pow(x,y))

import math

print(math.sqrt(25))

print(round(2.4566, 2))
print(round(2.4566, 3))

from math import floor, ceil

print(floor(2.4566))
print(ceil(2.4566))

print(divmod(10,4))

numero = 70 
caractere =  chr(numero)
print('O numero %d é mapeado para o caractere %s' % (numero,caractere))

for i in range(1,100):
    caractere = chr(i)
    print('%d - %s' % (i,caractere), end = '\n')

caractere = 'F'
numero = ord(caractere)
print ('O caractere %s é mapeado para o numero %d   ' % (caractere,numero,))