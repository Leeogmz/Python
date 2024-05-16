import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('Avançando em Data Science com Python\Data Visualization criando gráficos com bibliotecas Python\imigrantes_canada.csv')

df.set_index('País', inplace = True)

anos = list (map(str, range (1980,2014)))

brasil = df.loc['Brasil', anos]

brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}

dados_brasil = pd.DataFrame(brasil_dict)

fig = px.line(dados_brasil, x='ano', y='imigrantes',
              title='Imigração dos Brasil para o Canadá no período de 1980 a 2013')
fig.update_traces(line_color='green', line_width=4)
fig.update_layout(width=1000,height=500,
                  xaxis={'tickangle': -45},
                  font_family = 'Arial',
                  font_size=14,
                  font_color='grey',
                  title_font_color='black',
                  title_font_size=22,
                  xaxis_title='Ano',
                  yaxis_title='Número de imigrantes')


fig.show()