#situacao = [res_if if cond else res_else for item in lista] exemplo

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado" if media >= 6 else "Reprovado "for media in medias]

#cadastro = [expressao for item in listas]
cadastro = [x for x in [nomes, notas, medias]]

lista_completa = [nomes, notas, medias, situacao]
print(lista_completa)

