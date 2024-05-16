import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('Avançando em Data Science com Python\Data Visualization criando gráficos com bibliotecas Python\imigrantes_canada.csv')

df.set_index('País', inplace = True)

anos = list (map(str, range (1980,2014)))

america_sul = df.query('Região == "América do Sul"')

df_america_sul_clean = america_sul.drop(['Continente', 'Região', 'Total'], axis=1)

america_sul_final = df_america_sul_clean.T

fig =px.line(america_sul_final, x=america_sul_final.index, y=america_sul_final.columns, color='País',
             title='Imigração dos países da América do Sul para o Canadá de 1980 a 2013', markers=True)
fig.update_layout(
    xaxis={'tickangle': -45},
    xaxis_title='Ano',
    yaxis_title='Número de imigrantes'
)

fig.show()