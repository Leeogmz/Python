#Faça um programa, com uma função, que calcula a média de uma lista.

def calcular_media_lista():
    lista = []
    numero = input('Adicione um número na lista! ("0" para sair) ')

    while numero != '0':
        lista.append(int(numero)) 
        numero = input('Você quer adicionar outro número na lista? ("0" para sair) ')
    
    print(lista)

    if len(lista) > 0:
        media = sum(lista) / len(lista)
        print(f'A média dos números inseridos é: {media}')
    else:
        print('A lista está vazia, não é possível calcular a média.')

calcular_media_lista()