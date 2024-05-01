def soma(numero_1, numero_2):
    return numero_1 + numero_2

print(soma(17,3))

def media(lista_de_numeros):
    return sum(lista_de_numeros)/len(lista_de_numeros)

print(media([1,2,3,4]))

def imprime_relatorio(nome, cpf, telefone):
    return f"""
    Relátorio parcial
    {nome}, portador do {cpf}, que usa o número {telefone}
    Está oficialmente de férias
    Ass. Direção
"""
    
print(imprime_relatorio('Leonardo Gomes', 99999999999, 79999999999))