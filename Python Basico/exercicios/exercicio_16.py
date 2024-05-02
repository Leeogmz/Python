#Faça um programa, com uma função, que calcula a mediana de uma lista.

def calcular_mediana_lista():
    lista = []
    numero = input('Adicione um número na lista! ("0" para sair) ')

    while numero != '0':
        lista.append(int(numero)) 
        numero = input('Você quer adicionar outro número na lista? ("0" para sair) ')
    
    print(lista)

    if len(lista) > 0:
        lista_ordenada = sorted(lista)
        if len(lista) % 2 == 1:        
            mediana = lista_ordenada[len(lista) // 2]
        else:
            meio1 = lista_ordenada[len(lista) // 2 - 1]
            meio2 = lista_ordenada[len(lista) // 2]
            mediana = (meio1 + meio2) / 2
        
        print(f'A mediana dos números inseridos é: {mediana}')
    else:
        print('A lista está vazia, não é possível calcular a mediana.')

calcular_mediana_lista()   