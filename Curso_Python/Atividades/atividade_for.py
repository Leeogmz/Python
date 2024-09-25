#1° 

string = input('Digite um texto: ')
soma = 0

for i in string:
    if i != " ":
        soma += 1
print(soma)    
     
#2°

fatorial = int(input('Digite o fatorial desejado: '))
resultado = 1

for i in range(1, fatorial+1):
    resultado *= i

print('O fatorial de %d é %d ' % (fatorial, resultado))    

#3°

numero_de_leituras = int(input('Digite o número de textos que serão lidos: '))
texto_total = ''

for i in range(numero_de_leituras):
    texto_total += input('Digite o texto: ')
print('Texto completo: ', texto_total)    

#4°

numero = int(input('Digite a tabuada de divisão desejada: '))

for num in range (1,11):
    print('%d / %d = %f' % (num, numero, num /numero))

#5° 

for numero in range(3,31):
    e_primo = True
    for num_teste in range(2, numero):
        if (numero % num_teste == 0):
            e_primo = False
            break
    if e_primo:
        print('O número %d é primo ' % (numero))
    else: 
        print('O numero %d não é primo ' % (numero))        