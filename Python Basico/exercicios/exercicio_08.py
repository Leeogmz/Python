"""Exercício #8
Faça um programa que receba uma data de nascimento (15/07/87) e imprima
'Você nasceu em <dia > de <mês > de <ano>'"""

mensagem = input('Escreva sua data de nascimento! (00/00/00)')

dia, mes, ano = mensagem.split('/')

print(f'Você nasceu em {dia} de {mes} de {ano}')