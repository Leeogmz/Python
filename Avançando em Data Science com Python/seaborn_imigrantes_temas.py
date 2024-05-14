import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Avançando em Data Science com Python\\Data Visualization criando gráficos com bibliotecas Python\\imigrantes_canada.csv')

df.set_index('País', inplace = True)

anos = list (map(str, range (1980,2014)))

sns.set_theme(style='dark')
sns.set_theme(style='whitegrid')
sns.set_theme(style='white')
sns.set_theme(style='ticks')

top_10 = df.sort_values('Total', ascending=False).head(10)

def gerar_grafico_paleta(palette):
    fig, ax = plt.subplots(figsize=(8,4))
    ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h', palette=palette)
    ax.set_title('Países com maior imigração para o Canadá\n1980 a 2013', loc='left', fontsize=18)
    ax.set_xlabel('Número de imigrantes', fontsize=14)
    ax.set_ylabel('')

gerar_grafico_paleta('tab10')


fig, ax = plt.subplots(figsize=(8,4))
ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h', palette='tab10')
ax.set_title('Países com maior imigração para o Canadá\n1980 a 2013', loc='left', fontsize=18)
ax.set_xlabel('Número de imigrantes', fontsize=14)
ax.set_ylabel('')
sns.despine()

plt.show()