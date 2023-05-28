from random import randint

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]

def gera_codigo():
  return str(randint(0,999))

codigo_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

print(codigo_estudantes)    


