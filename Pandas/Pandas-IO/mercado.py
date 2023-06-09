import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'

dados_mercado = pd.read_csv(url, sep=',')

dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])

dados_selecao.to_csv('dados_mercado.csv', sep=';', index=False)


clientes_mercado = pd.read_csv('dados_mercado.csv', sep=';')

print(dados_mercado.head())
print(dados_selecao.head())
print(clientes_mercado.head())

