"""Exercício # 12
Faça um programa que receba uma string, com um número de ponto flutuante, 
imprima qual a parte dele que não é inteira
EX:
n ='3.14'
resposta: 14  """ 

string = input('Escreva um numero float! ')

inteiro, flutuante = string.split('.')

print(flutuante)