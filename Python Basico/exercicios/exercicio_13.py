"""Exercício #13
Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
e um número inteiro, imprima a tabuada desse número."""


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = int(input('Insira um numero inteiro! '))

for n in lista:
    print(f'{numero} x {n} = {numero * n}')