import pandas as pd
import matplotlib as plt
import numpy as np
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import poison

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

probabilidade = (np.e(-media)*(media**k))/(np.math.factorial(k))
                 
probabilidade = poison.pmf(k, media)

print('%0.8f' % probabilidade_de_passar3)
