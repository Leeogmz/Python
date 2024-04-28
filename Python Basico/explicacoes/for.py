"""
for elemento in iteravel:
    faça algo
para cada 'elemento' dentro do iteravel:
    faça algo
"""

palavra = input('Escreva uma palavra! ')

for posicao, letra in enumerate(palavra):
    print(posicao, letra)