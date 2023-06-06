#1) Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

for lista in lista_de_listas:
    print(sum(lista))


#2) Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:


lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

lista2 = []
for tupla in lista_de_tuplas:
    lista2.append(tupla[2])
print(lista2)


#3) A partir da lista, crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.


lista3 = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_de_tuplas2 = []


for i in range(len(lista3)):
    lista_de_tuplas2.append((i, lista3[i]))
print(lista_de_tuplas2) 


#4) Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

lista4 = [tupla[1] for tupla in aluguel if tupla[0]== 'Apartamento']
print(lista4)

#5) Crie um dicionário usando o dict comprehension

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] 
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
print(dicionario)

#6) Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código:

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

filtro = [tupla[1] for tupla in vendas if tupla[0] == '2022' and tupla[1] > 6000]
print(filtro)
