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