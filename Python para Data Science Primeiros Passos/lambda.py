#formato padrão > lambda<variavel>: <expressao>


n1 = float(input("Digite a 1° nota do(a) estudante: "))
n2 = float(input("Digite a 2° nota do(a) estudante: "))
n3 = float(input("Digite a 3° nota do(a) estudante: "))


media_ponderada = lambda x, y, z: (x*3 + y*2 + z*5)/10

media_estudante = media_ponderada(n1, n2, n3)

print(f'O(a) estudante atingiu uma média de {media_estudante}')


#agora vamos acrescentrar 0.5 extra a essas notas usando a função map lambda e list
notas = [n1, n2, n3]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)



print(list(notas_atualizadas))




