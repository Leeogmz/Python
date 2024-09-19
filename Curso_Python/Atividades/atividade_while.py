#1° 

soma = 0
numeros_lidos = 0

while (numeros_lidos < 5):
    num = float(input('Digite um valor: '))
    soma += num
    numeros_lidos += 1
media = soma / 5    

print('A media é: %.2f' % media)

#2° 

soma = 0
numeros_lidos = 0

while (numeros_lidos < 5):
    num = float(input('Digite um valor: '))
    if num >= 0:
        soma += num
    numeros_lidos += 1

print('A soma é: %.2f' % soma)

#3

numes_que_devem_ser_lidos = float(input('Digite quantos números serão lidos: '))
soma = 0
numeros_lidos = 0

while (numeros_lidos < numes_que_devem_ser_lidos):
    num = float(input('Digite um valor: '))
    if num >= 0:
        soma += num
    numeros_lidos += 1

print('O total é: %.2f' % soma)

#4

num_atual = 2

while (num_atual <= 10):
    resto = (num_atual % 2)
    if resto == 0:
        print('O número %d é par' % (num_atual))
    else:
        print('O número %d é impar' % (num_atual))
    num_atual += 1

#5

texto = input('Digite um texto: ')
indice = 0
num_vazio = 0

while (indice < len(texto)):
    if texto[indice] == " ":
        num_vazio += 1
    indice += 1
print('O número de espaços no texto é de %d ' % (num_vazio))    