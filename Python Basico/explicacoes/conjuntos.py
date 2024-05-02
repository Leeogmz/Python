A = {'Leonardo', 'Leonardo'}
lista = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4]
lista = list(set(lista))

print(A)
print(lista)
print(A.union({'Outra pessoa', 'Leonardo'}))
print(A.difference({'Outra pessoa', 'Leonardo'}))
print(A.intersection({'Outra pessoa', 'Leonardo'}))