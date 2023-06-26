import pandas as pd

url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url,delimiter=";")

print(dados.head()) #.head() para trazer as primeiras 5 linhas e .tail() para trazer as ultimas 5 linhas (caso precise trazer mais ou menos linhas basta inluir esse valor dentro do parametro da função)

print(dados.shape)
