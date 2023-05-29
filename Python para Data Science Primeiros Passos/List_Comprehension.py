# 3.2 List comprehension - É uma forma simples e concisa de criar uma lista. Podemos aplicar condicionais e laços para criar diversos tipos de listas a partir de padrões que desejamos para a nossa estrutura de dados. 



nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

medias = [round(media(nota),1) for nota in notas]

print(medias)

nomes = [nome[0] for nome in nomes]
print(nomes)

estudantes = list(zip(nomes, medias))

print(estudantes)