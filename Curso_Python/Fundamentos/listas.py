array = []
array = list()
array_numeros = [1,2,3]
array_floats = [56.3, -2.2, 0.5]
array_str = ['A', 'B', 'C']
array_misto = [2, 2.3, 'ABC']

print(array) 
print(array_numeros) 
print(array_floats)
print(array_str)
print(array_misto)

array = list([1,2,3])
print(array)

primeiro_elemento = array[0]
print(primeiro_elemento)

array[0] = 20
primeiro_elemento = array[0]
print(primeiro_elemento)
print(array[-1])
print(array)

array = [1, 'texto', 3]

print(array[1:3])

array = [10,2,3]
print(array)
array.append(2)
print(array)
array.insert(2, '4')
print(array)

array = [10,2,3,20,'3']
array.remove(10)
print(array)
array.pop(2)
print(array)
print(len(array))

array.clear()
print(array)

array = [1, 'teste', 1.3, True]

print(1 in array)
print(False not in array)

lista = [5,6,7,2,3,4,7]
teste = lista.count(7)
print(teste)
pos = lista.index(5)
print(pos)

array1 = [1,2,3]
array2 = [3,4,5]
soma = array1 + array2
print(soma)

mult = array1 * 3
print(mult)

numeros = ['um', 'dois', 'três']
x,y,z = numeros
print(x)
print(y)
print(z)

x,y,_ = numeros
print(x)
print(y)

cores = ['azul', 'preto', 'amarelo']
for x in cores:
    print(x)

print('____________')

cores = ['azul', 'preto', 'amarelo']
for i in range(0, len(cores)):
    print(cores[i])

print('____________')

cores = ['azul', 'preto', 'amarelo']
indice = 0

while (indice <  len(cores)):
    print(cores[indice])
    indice += 1

lista = [[1,2,3], [4,5,6]]

primeira_lista = lista[0]
segunda_lista = lista[1]

print(primeira_lista)
print(segunda_lista)

primeiro_elemento_primeira_lista = lista[0][0]
print(primeiro_elemento_primeira_lista)

#SET

lista_set = {}
lista2_set = {1,2,3}
lista3_set = set({1,2,3})

print(lista_set)
print(lista2_set)
print(lista3_set)

lista_set = {1,2,3}
lista_set.add(5)
print(lista_set)
lista_set.remove(1)
print(lista_set)

#Não permite duplicados
lista_set = {1,2,3,4,2}
lista_set.add(1)
print(lista_set)

lista_set = {1,2,3,4}
lista_set.clear()
print(lista_set)

lista_set = {1,2,3,4}
print(len(lista_set))
print(1 in lista_set)

lista_set = {1,2,3,'4', True, 6.1}
for item in lista_set:
    print(item)

# na memoria 1 = True e 0 = False, por isso no primeiro exemplo nao aparece True devido entender que há duplicata    

lista_set = {2,3,'4', True, 6.1}
for item in lista_set:
    print(item)    

set1 = {1,2,3}
set2 = {1,2,3,4}
set_unido = set1.union(set2)
print(set_unido)

set1 = {1,2,3}
set2 = {3,4,5,6}
set_unido = set1.union(set2)
print(set_unido)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_inter = set1.intersection(set2)
print(set_inter)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_dif = set2.difference(set1)
print(set_dif)