notas = {'1° trimestre:': 8.5, '2° trimestre:': 9.5, '3° trimestre:': 7 }

soma = sum(notas.values())

qtd_notas = len(notas)

print (soma)
print(qtd_notas)

media = soma / qtd_notas

media = round(media, 2)

print(media)


def media ():
    calculo =(10 + 9.5 + 8)/3

    print(calculo)

def media(nota_1, nota_2, nota_3):
    calculo = (nota_1 + nota_2 + nota_3) /3
    print(calculo)


nota1 = 10
nota2 = 9
nota3 = 10

media (nota1, nota2, nota3)




notas = [9.5, 5.5, 7.5]


def mediaList(lista):
    calculo = sum(lista)/len(lista)
    print (calculo)


mediaList(notas)    


