#TUPLES
#Tuplas sao imutaveis

doces = tuple(('chocolate', 'bom bom', 'paçoca'))
print(doces)

doces = ('chocolate', 'bom bom', 'paçoca')
print(doces)

nums = ('1', '2', '3')
print(len(nums))
print(nums[2])

nums = (1,2,3,4,5,6,7,8)
sub_tupla = nums[2:4]
print(sub_tupla)
print(4 in nums)

"""
tupla = tuple((10,20,40))
tupla[0] = 20
    
TypeError: 'tuple' object does not support item assignment """

tupla = (6,7,8,9,10,6,6)
print(tupla.count(6))

tupla = (5,'3',True, 7234)
pos = tupla.index('3')
print(pos)

for x in tupla:
    print(x)

for i in range(0, len(tupla)):
    print(tupla[i])

indice = 0

while indice < len(tupla):
    print(tupla[indice])
    indice += 1

numeros_set = (1,2,3)
numeros_lista = list(numeros_set)
numeros_lista[0] = 12
numeros_lista.append('Fim')
numeros_set = tuple(numeros_lista)
print(numeros_set)    