lista = ['Fabricio Daniel', 9.5, 9.0, 8.0, True ]


lista[3] += 2   

for elemento in lista:
    print(elemento)


media = (lista[1] + lista[2] + lista[3]) / 3
print(media)

print(len(lista)) #Para saber a quantidade de itens em uma lista

listaNotas = lista[1:4] #partição de lista

print(len(listaNotas))

media2 = (lista[1] + lista[2] + lista[3]) / len(listaNotas) #fazendo a media com a quantidade de itens da lista

print(media2)

lista.append(media) #adiciona 1 unico  elemento ao final da lista

print(lista)

lista.extend([10.0, 8.0, 9.0]) #adiciona varios elementos separados ao final da lista

print(lista)

lista.append([10.0, 8.0, 9.0])
print(lista)

lista.remove([10.0, 8.0, 9.0]) #para remover elementos da lista
print(lista)