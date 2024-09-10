numero = 1
if numero ==1 or numero ==0:
    print('É 1 ou 0')

numero = 11
condicao = numero > 10 or numero < -10
if condicao:
    print('absolutamente maior que 10')

numero = 12
if numero > 0:
    print('Número é maior que 0')
    if numero > 10:
        print('Número é maior que 10')

numero = 11
if numero < 10:
    print('menos que 10')
elif numero < 100:
    print('menos que 100')
elif numero <= 1000:
    print('menor ou igual a 1000')
elif numero < 10:
    print('Nenhuma anterior')

texto = 'b'
if texto == 'a':
    print('É vogal a')
elif texto == 'e':
    print('É vogal e')
elif texto == 'i':
    print('É vogal i')
elif texto == 'o':
    print('É vogal o')
elif texto == 'u':
    print('É vogal u')
else: 
    print('É consoante')

numero = 15
resultado = 'PAR' if numero % 2 == 0 else 'IMPAR'
print(resultado)

numero = 3
resultado = 'Um' if numero == 1 else 'Dois' if numero == 2 else 'Três'
print(resultado)