import pandas as pd
import matplotlib as plt
import numpy as np
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm


dados = pd.read_csv('Estatística com Python\\Probabilidade e amostragem\\dados.csv')

n = 10

numero_de_alternativas_por_questao = 3

p = 1 / numero_de_alternativas_por_questao

q = 1 - p

k = 5

probabilidade = (comb(n,k)*(p**k)*(q**(n-k)))

print('%0.8f' % probabilidade)

probabilidade2 = binom.pmf(k,n,p)

probabilidade_de_passar = binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()

probabilidade_de_passar2 = 1 - binom.cdf(4,n,p)

probabilidade_de_passar3 = binom.sf(4,n,p)

p = 0.60
n = 12 
k = 8

probabilidade = binom.pmf(k,n,p)

equipes = 30 * probabilidade

media = 20
k = 15

probabilidade3 = (np.e ** (-media) * (media ** k)) / np.math.factorial(k)
                 
probabilidade4 = poisson.pmf(k, media)

tabela_normal_padronizada = pd.DataFrame(
    [], 
        index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
        columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

print(tabela_normal_padronizada)

media = 1.7

desvio_padrao = 0.1

z = (1.8 - media) / desvio_padrao

probabilidade5 = 0.8413

probabilidade6 = norm.cdf(z)

print(probabilidade6)