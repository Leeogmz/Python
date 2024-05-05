import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Avançando em Data Science com Python\Data Visualization criando gráficos com bibliotecas Python\imigrantes_canada.csv')

df.info()

df.set_index('País', inplace = True)

anos = list (map(str, range (1980,2014)))

brasil = df.loc['Brasil', anos]

brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}

dados_brasil = pd.DataFrame(brasil_dict)

print(dados_brasil)

plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
plt.xticks(['1980','1985', '1990','1995','2000','2005','2010'])
plt.title ('Imigração do Brasil para o Canadá')
plt.xlabel('Ano')
plt.ylabel ('Número de imigrantes')

df_comparacao = df.loc[['Brasil', 'Argentina'], anos]

df_comparacao = df_comparacao.T

plt.plot(df_comparacao['Brasil'],label = 'Brasil')
plt.plot(df_comparacao['Argentina'],label ='Argentina')
plt.title('Imigração do Brasil e Argentina para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.legend()

#Criando figura

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013')
ax.set_xlabel('Ano')
ax.set_ylabel('Número de imigrantes')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))

# criando subplots em uma direção
fig, axs = plt.subplots(1,2, figsize=(15,5))
axs[0].plot(dados_brasil['ano'], dados_brasil['imigrantes'])
axs[0].set_title('Imigração do Brasil para o Canadá\n1980 a 2013')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Número de imigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid()

axs[1].boxplot(dados_brasil['imigrantes'])
axs[1].set_title('Boxplot da imigração do Brasil para o Canadá\n1980 a 2013')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Número de imigrantes')
axs[1].grid()

print(dados_brasil.describe())

# criando subplots em duas direção

fig, axs = plt.subplots(2,2, figsize=(10,6))
fig.subplots_adjust(hspace=0.5, wspace=0.3)
fig.suptitle('Imigração dos quatro maiores países da América do Sul para o Canadá de 1980 a 2013')

axs[0,0].plot(df.loc['Brasil', anos])
axs[0,0].set_title('Brasil')

axs[0,1].plot(df.loc['Colômbia', anos])
axs[0,1].set_title('Colômbia')

axs[1,0].plot(df.loc['Argentina', anos])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Peru', anos])
axs[1,1].set_title('Peru')

for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))

for ax in axs.flat:
    ax.set_xlabel('Ano')
    ax.set_ylabel('Número de imigrantes')    

ymin = 0
xmax = 7000

for ax in axs.ravel():
    ax.set_ylim(ymin,xmax)  
    
plt.show()