"""Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.

Caso o(a) estudante não esteja matriculado(a) na turma devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma".  """


notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], 
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}



try: 
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
    
except KeyError:
    print("Estudante não matriculado(a) na turma") 
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!") 