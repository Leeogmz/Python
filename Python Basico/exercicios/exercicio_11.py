"""Exercício # 11
Faça um programa que itera em uma string e toda vez que uma vogal aparecer na sua string print o seu nome entre as letras
string = bananas
b
eduardo
n
eduardo"""

palavra = input('Escreva uma palavra! ')
vogais ='aeiouAEIOU'
nome = 'Leonardo'

""" for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(nome)
    else: 
        print(letra) """  


for letra in palavra:
    if letra in vogais:
        print(nome)
    else: 
        print(letra)    
