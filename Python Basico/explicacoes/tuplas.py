
minha_tupla = ('Leonardo', 26, 7999999999, 'Rua dos bobos', 0)

nome, idade, *coisas_que_nao_quero = minha_tupla

print(minha_tupla)
print(nome)
print(idade)
print(coisas_que_nao_quero)