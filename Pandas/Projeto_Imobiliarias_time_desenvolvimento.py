import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url,delimiter=";")

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']

dados['Valor_por_ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']

dados['Descricao'] = dados['Tipo'] + ' em ' +  dados['Bairro'] + ' com ' + dados['Quartos'].astype(str) + ' quarto(s) ' + ' e ' + dados ['Vagas'].astype(str) + ' vaga(s) de garagem.'

dados['Possui_suite'] = dados['Suites'].apply(lambda x: 'Sim' if x > 0 else 'Não')

dados.to_csv('dados_desenvolvimento.csv', index=False, sep=';')


print(dados.head())