""" crie um array, utilizando a função np.arange(), que liste todos os anos onde aconteceram ou estão previstos de acontecer a Copa do Mundo, 
considerando o intervalo fechado dos anos de 2000 a 2102."""

import numpy as np

ano_inicial = 2002
ano_final = 2102
print(np.arange(ano_inicial, ano_final + 1, 4))