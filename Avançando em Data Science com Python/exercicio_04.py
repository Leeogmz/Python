"""Bruna, uma profissional que atua em uma empresa de e-commerce, 
tem a responsabilidade de analisar as vendas de produtos do último ano. 
Para isso, ela coletou os dados de vendas em cada mês e armazenou em um DataFrame chamado df. 
Esse DataFrame, que contém as informações referentes às vendas de produtos, possui uma coluna com os meses e uma coluna chamada vendas, 
plot um grafico de barras com as informações do número total de vendas realizadas em cada mês."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas = [1200, 4100, 3800, 1000, 6000, 7000, 3800, 3700, 700, 2000, 5600, 8000]

df = pd.DataFrame({'mes': meses, 'vendas': vendas})

sns.barplot(data=df, x='mes', y='vendas')

plt.show()