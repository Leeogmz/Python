iteracao = 10

while (iteracao > 0):
    print(iteracao)
    iteracao -= 1
print('Encerrou!')

indice = 10
print('Programa começou!')
while (indice >= 2):
    resto = (indice % 2)
    if resto == 0:
        print('O número %d é par' % (indice))
    else:
        print('O número %d é impar' % (indice))
    indice -= 1
print('Programa encerrou!')


    