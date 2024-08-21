# 1°

ano_atual = 2024
ano_nascimento = 1997
estimativa_idade = (ano_atual - ano_nascimento)
print('Devo ter em torno de %d anos' % (estimativa_idade))

#2°
num1 = 5
num2 = 6
num3 = 8
media = ((num1+num2+num3)/3)
print('A media é %f' % media)

#3°

peso = 72
altura = 1.70
imc = peso // altura ** 2
print('O IMC é: ', imc)

#4°

ovos = 50
pessoas = 3
ovos_por_pessoa = (ovos // pessoas)
ovos_restantes = (ovos % pessoas)
print('Tenho inicialmente %d ovos para %d pessoas ' % (ovos, pessoas))
print('Cada uma das %d pessoas terá %d ovo(s)' % (pessoas, ovos_por_pessoa))
print('Restou %d ovo(s) que não puderam ser divididos' % (ovos_restantes))