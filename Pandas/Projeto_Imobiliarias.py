import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"
dados = pd.read_csv(url,delimiter=";")

print(dados.head()) #.head() para trazer as primeiras 5 linhas e .tail() para trazer as ultimas 5 linhas (caso precise trazer mais ou menos linhas basta inluir esse valor dentro do parametro da função)

print(dados.shape)

print(dados.columns)

dados.info()

print(dados[['Quartos', 'Valor']])

print(dados['Valor'].mean())

#print(dados.groupby('Tipo').mean(numeric_only = True)) para trazer a media somente das colunas do tipo numeric


df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

#df_preco_tipo.plot(kind='barh', figsize=(14,10), color ='Blue')
#plt.show()

#print(dados.Tipo.unique()) para pegar os dados sem repetição de uma coluna

imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Box/Garagem' ,'Chácara',
                      'Loja Shopping/ Ct Comercial',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé','Hotel', 'Indústria']

df = dados.query('@imoveis_comerciais not in Tipo')

df.head()

print(df.Tipo.unique())

df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

df_preco_tipo.plot(kind='barh', figsize=(14,10), color ='Blue')
#plt.show()

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')


df_percentual_tipo.plot(kind='bar', figsize=(14,10), color ='Green', xlabel = 'Tipos', ylabel = 'Percentual')
#plt.show()

df = df.query('Tipo == "Apartamento"')

print(df.head)

#1) Calcular a média de quartos por apartamento;
print(df['Quartos'].mean())

#2) Conferir quantos bairros únicos existem na nossa base de dados;
print(len(df['Bairro'].unique()))

#3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas;
print(df.groupby('Bairro')[['Valor']].mean().sort_values('Valor'))

#4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.
df_bairros = df.groupby('Bairro')[['Valor']].mean().sort_values('Valor').tail()

print(df_bairros)

df_bairros.plot(kind='barh', figsize=(14,10), color='blue'); 
plt.show()






