import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url,delimiter=";")

df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

imoveis_comerciais = ['Conjunto Comercial/Sala','Prédio Inteiro','Loja/Salão','Galpão/Depósito/Armazém','Casa Comercial','Terreno Padrão','Box/Garagem','Chácara','Loja Shopping/ Ct Comercial','Loteamento/Condomínio','Sítio','Pousada/Chalé','Hotel','Indústria']

df = dados.query('@imoveis_comerciais not in Tipo') #Para retirar os imoveis comerciais da base de dados

df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')

df = df.query('Tipo == "Apartamento"')

df = df.fillna(0)

registros_a_remover = df.query('Valor==0 | Condominio ==0').index #Para filtrar os itens zerados

df.drop(registros_a_remover, axis=0, inplace=True) #Para remover as linhas com os itens zerados 

df.drop('Tipo', axis=1, inplace=True) #Removendo a coluna Tipo

df.to_csv('dados_apartamento.csv', index=False, sep=';')