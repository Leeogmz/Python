import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url,delimiter=";")

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']

dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']

print(dados.head())
