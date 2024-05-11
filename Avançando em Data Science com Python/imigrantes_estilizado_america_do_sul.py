import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Avançando em Data Science com Python\Data Visualization criando gráficos com bibliotecas Python\imigrantes_canada.csv')

df.set_index('País', inplace = True)

anos = list (map(str, range (1980,2014)))

brasil = df.loc['Brasil', anos]

brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}

dados_brasil = pd.DataFrame(brasil_dict)

america_sul = df.query('Região == "América do Sul"')
america_sul_sorted = america_sul.sort_values('Total', ascending=True)

#cores = ['royalblue', 'orange', 'forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']

cores=[]

for pais in america_sul_sorted.index:
    if pais == 'Brasil':
        cores.append('green')
    else:
        cores.append('silver')

fig, ax = plt.subplots(figsize=(12,5))
ax.barh(america_sul_sorted.index, america_sul_sorted['Total'], color=cores)
ax.set_title('América do sul: Brasil foi o quarto país com mais imigrantes\npara o Canadá, no período de 1980 a 2013', loc='left', fontsize=18)
ax.set_xlabel('Número de imigrantes', fontsize=14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

for i, v in enumerate(america_sul_sorted['Total']):
    ax.text(v + 100, i , str(v), color='black', fontsize=10, ha='left', va='center')

ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
ax.tick_params(axis='both', which='both', length=0)

print(fig.canvas.get_supported_filetypes())

fig.savefig('imigracao_america_sul.png', transparent=False, dpi=300, bbox_inches='tight')

plt.show()