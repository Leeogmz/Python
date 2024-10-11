#1°

objetos = {
    'faca' : 'serve para cortar', 
    'cadeira' : 'serve para sentar', 
    'roupa' : 'serve para vestir'   
    }

objeto_procurado = input('Qual objeto voê quer saber a função? ')

if objeto_procurado in objetos:
    print(objetos[objeto_procurado])
else:
    print('Objeto não foi encontrado!')    

#2°

lista_negativos = []

for x in range(-30,-19):
    lista_negativos.append(x)

print(lista_negativos)

#3°

lista = [x for x in range(4,101) if x % 4 == 0]
print(lista)

#4°

lista = [ x for x in range(0,101) if str(x)[-1] == '0' ]
print(lista)

#5°

lista = [ '0' if str(x)[-1] == '0' else '-' for x in range(0,21) ]
print(lista)