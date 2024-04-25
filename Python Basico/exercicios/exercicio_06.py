"""Exercício #6
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato."""

produto_1 = float(input('Insira o preço do 1° produto: '))
produto_2 = float(input('Insira o preço do 2° produto: '))
produto_3 = float(input('Insira o preço do 3° produto: '))




if produto_1 < produto_2 and produto_1 < produto_3:
    print('Compre o produto 1')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print('Compre o produto 2')
else:
    print('Compre o produto 3')    
