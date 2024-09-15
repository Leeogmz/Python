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

soma = 0
numeros_lidos = 0

while (numeros_lidos < 5):
    num = float(input('Digite um valor: '))
    soma += num
    numeros_lidos += 1

print('Soma é: %.2f' % soma)


texto = 'Olá 123 _'
indice = 0

while (indice < len(texto)):
    print(texto[indice])
    indice += 1