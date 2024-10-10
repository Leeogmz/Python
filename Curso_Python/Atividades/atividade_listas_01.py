#1° 
lista = [1,10,6,7,8,10]
soma = 0
for x in lista:
    soma += x
    print(soma)

#2°

lista = []

for x in range(1,101):
    lista.append(x)
print(lista)

#3°

lista1 = {0,4,43,52,65,-10}
lista2 = {43,2,4,76,32,65,3}

lista_combinada = lista1.union(lista2)
print(lista_combinada)

"""#4°

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

mes_nascimento = int(input('Em qual mês você nasceu? '))

print('Você nasceu no mês: %s ' % (meses[mes_nascimento -1 ]))  """  


#5° 

dias = []

for x in range(1,32):
    dias.append(x)

dia_nascimento = int(input('Em que dia você nasceu? '))

dias.remove(dia_nascimento)
print(dias)    
