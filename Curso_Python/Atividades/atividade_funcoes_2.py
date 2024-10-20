#1°
def encontra(array, item):
    for i in array:
        if i == item:
            return True
    return False     

arra = [3,1,2,"Olá", 1.2]   

print(encontra(arra,"Olá"))
print(encontra(arra,"abc"))
print(encontra(arra,2))

#2°

def encontra_indice(array, item):
    for i in range(0,len(array)):
        if array[i] == item:
            return True, i+1
    return False, -1     

arra = [3,1,2,"Olá", 1.2]   

print(encontra_indice(arra,"Olá"))
print(encontra_indice(arra,"abc"))
print(encontra_indice(arra,2))

#3°
def mostra_tipo(*args):
    for i in args:
        print(type(i))

mostra_tipo(1,2,3,"Texto",True)        

#4°

def citacao(func):
    def func_inner(str):
        return '"' + func(str).lower() + '"'
    return func_inner 

@citacao
def trasnforma(str):
    return str

print('E disse joão', trasnforma('Só os sábios sabem!'))       

#5°
def printa_div_3(num):
    if num == 11:
        return
    print(num//3)
    printa_div_3(num+1)

printa_div_3(0)    
