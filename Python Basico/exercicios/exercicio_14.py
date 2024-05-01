"""Exercício #14
Faça uma programa que dada a entrada de uma lista ele faça o cálculo
acumulativo da mesma:
Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: [1, 3, 6, 10]"""

entrada = [1,2,3,4]
saida = []
soma = 0

for elemento in entrada:
    soma += elemento
    saida.append(soma)
    print(saida)