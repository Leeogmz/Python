#1°

media_input = input('Digite sua média nas provas: ')
exame_input = input('Digite sua nota no exame: ')
media_prova = int(media_input)
nota_exame = int(exame_input)
aprovado = (media_prova >= 7) or (nota_exame >= 5)
print('Aprovação: ', aprovado)

#2°

senha = '1234'
tentativa = input('Digite a senha: ')
print('Senha está correta? ', senha == tentativa)