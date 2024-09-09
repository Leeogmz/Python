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