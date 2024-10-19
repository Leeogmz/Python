#1°
def e_negativo(numero):
    return numero < 0

print(e_negativo(2))
print(e_negativo(-2))

#2°

def soma(arr):
    soma=0
    for i in arr:
        soma += i
    return soma
print(soma([10,20,40]))

#3°

def conta_vogais(texto):
    vogais =0
    arr_vogais = ('a','e','i','o','u')
    for i in texto:
        if i in arr_vogais:
            vogais += 1
    return vogais      

print(conta_vogais('alterações'))  

#4°

def ultimo_caractere(texto):
    return texto[-1]

print(ultimo_caractere('Python 4'))

#5°

def calculadora(num1, num2, op):
    def soma(a,b):
        return a+b
    def subtrai(a,b):
        return a-b
    if op == '+':
        return soma(num1,num2)
    elif op == '-':
        return subtrai(num1,num2)
    
print(calculadora(10,30,'+'))