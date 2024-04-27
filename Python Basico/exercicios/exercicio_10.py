"""Exercício #10
Faça um programa que leia 5 números e informe o maior número."""


numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))
numero3 = float(input("Digite o 3º número: "))
numero4 = float(input("Digite o 4º número: "))
numero5 = float(input("Digite o 5º número: "))

maior_numero = numero1
if numero2 > maior_numero:
    maior_numero = numero2
if numero3 > maior_numero:
    maior_numero = numero3
if numero4 > maior_numero:
    maior_numero = numero4
if numero5 > maior_numero:
    maior_numero = numero5

print(f'O maior número é: {maior_numero}')
