#1) Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

for lista in lista_de_listas:
    print(sum(lista))


#2) Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:


lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista2 = []
for tupla in lista_de_tuplas:
    lista2.append(tupla[2])
print(lista2)


#3) A partir da lista, crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.


lista3 = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_de_tuplas2 = []


for i in range(len(lista3)):
    lista_de_tuplas2.append((i, lista3[i]))
print(lista_de_tuplas2) 

