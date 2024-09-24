
for x in range(10):
    print(x)

print('______________')
for w in range(5,10):
    print(w)      

print('______________')
for w in range(5,20,5):
    print(w)    

print('______________')
for w in range(20,5,-5):
    print(w)    

print('______________')

texto ='123456789'
for x in range(0, len(texto)):
    print(texto[x])

print('______________')

letra = input('Digite uma letra: ')

if (len(letra) != 1):
    print('Precisa ter 1 digito! ')
else:
    texto = input ('Digite um texto: ') 
    for i in range(0,len(texto)):
        if letra == texto[i]:
            print('Encontei a letra " %s " na posição %d ' % (letra, i))

texto = 'Olá, eu sou iterável'

for x in texto:
    print(x)

for x in range(0,3):
    for y in range(0,5):
        print(x,y)

for x in range(1,11):
    print('______________________')
    for y in range(1,11):
        print('%d X %d = %d' % (x,y, x*y))        