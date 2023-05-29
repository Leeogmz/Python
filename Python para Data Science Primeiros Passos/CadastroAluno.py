nome = input('Escreva o nome do aluno(a): ')

ano_entrada = int(input('Escreva o ano de ingresso do(a) aluno(a): '))

media = float(input('Digite a media do aluno(a): '))

if media >= 6.0:
    situacao = 'Aprovado (a)'
elif 6.0 > media >= 4.0:
    situacao = 'Pode realizar a prova de recuperação'         
else: situacao = 'Reprovado (a)'

               

print('Nome do aluno é: %s, ele ingressou no ano de: %d, e tem média de: %f, portanto sua situação é: %s' %(nome, ano_entrada, media, situacao))