lista_de_compras = []
resposta = ''

while resposta != 'acabou':
    resposta = input('O que temos que comprar? ')
    if resposta != 'acabou':
        lista_de_compras.append(resposta)

print(lista_de_compras)