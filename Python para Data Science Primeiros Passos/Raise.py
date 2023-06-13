''' Você criou uma função para calcular a média de um estudante em uma dada matéria passando em uma lista as notas deste estudante. 

Você pretende tratar 2 situações:
- Se a lista possuir um valor não numérico o cálculo de média não será executado e uma mensagem de "Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!" será exibida.
- Caso a lista tenha mais de 4 notas, será lançada uma exceção do tipo **ValueError** informando que "A lista não pode possuir mais de 4 notas." 

Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada. '''


def media(lista: list=[0]) -> float:
  
  calculo = sum(lista) / len(lista)
  if len(lista) > 4:
   raise ValueError("A lista não pode possuir mais de 4 notas. ")
  return calculo

try:
    notas = [0,0,0,0]
    
    for i in range(len(notas)):
      notas[i] = float(input("Insira a nota: "))

    resultado = media(notas)
except TypeError:
  print("Não foi possivel calcular a média do estudante, só são aceitos valores numericos.")    
except ValueError as e:
  print(e)
else:  
    print(resultado)
finally:
   print("A consulta foi encerrada!")
