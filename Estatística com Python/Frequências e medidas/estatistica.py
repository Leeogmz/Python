import pandas as pd
import numpy as np
import seaborn as sns
import scipy
import matplotlib.pyplot as plt


dados = pd.read_csv('Estatística com Python\Frequências e medidas\dados.csv')

print(sorted(dados['Anos de Estudo'].unique()))

print(sorted(dados['UF'].unique()))

print(sorted(dados['Sexo'].unique()))

print(sorted(dados['Cor'].unique()))

print('A idade varia de %s até %s anos' % (dados['Idade'].min(),dados['Idade'].max()))

#Distribuição de frequências para variáveis qualitativas

frequencia = dados['Sexo'].value_counts()

percentual = dados['Sexo'].value_counts(normalize=True) * 100

dist_freq_qualitativas = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem (%)':percentual})

dist_freq_qualitativas.rename(index={0: 'Masculino' , 1: 'Feminino'}, inplace=True)

dist_freq_qualitativas.rename_axis('Sexo', axis='columns',inplace=True)

sexo = {0: 'Masculino',
        1: 'Feminino'}

cor = {0: 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8: 'Parda',
        9: 'Sem declaração'}

frequencia_sexo_cor = pd.crosstab(dados.Sexo,
                         dados.Cor)
frequencia_sexo_cor.rename(index = sexo, inplace = True)
frequencia_sexo_cor.rename(columns = cor, inplace = True)


percentual_sexo_cor = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         normalize=True) * 100
percentual_sexo_cor.rename(index = sexo, inplace = True)
percentual_sexo_cor.rename(columns = cor, inplace = True)

classes = [0, 1576, 3152, 7880, 15760, 200000]

labels = ['E', 'D', 'C', 'B', 'A']

frequencia_renda = pd.value_counts(
    pd.cut(dados.Renda,
       bins = classes,
       labels= labels,
       include_lowest= True)
)

percentual_renda = pd.value_counts(
    pd.cut(dados.Renda,
       bins = classes,
       labels= labels,
       include_lowest= True),
       normalize=True
)

dist_freq_quantitativas_personalizadas = pd.DataFrame(
    {'Frequencia': frequencia_renda, 'Porcentagem (%)':percentual_renda}
)

dist_freq_quantitativas_personalizadas = dist_freq_quantitativas_personalizadas.sort_index(ascending=False)

n = dados.shape[0]

k = 1 + (10/3) * np.log10(n)

k = int(k.round(0))

frequencia2 = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = k,
        include_lowest=True
    ),
    sort=False
)

percentual2 = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = k,
        include_lowest=True
    ),
    sort=False,
    normalize=True
)

dist_freq_quantitativas_amplitude_fixa = pd.DataFrame(
    {'Frequencia': frequencia2, 'Porcentagem (%)':percentual2}
)


print(dist_freq_quantitativas_amplitude_fixa)

ax = sns.distplot(dados.Altura)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)

ax.figure.set_size_inches(12, 6)
ax.set_title('Distribuição de Frequências - Altura - KDE ', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)

dist_freq_quantitativas_personalizadas['Frequencia'].plot.bar(width=1, color='blue', alpha=0.2, figsize= (12, 6))

renda_media = dados.Renda.mean()

renda_media_por_sexo = dados.groupby('Sexo')['Renda'].mean()

renda_mediana = dados.Renda.median()

renda_moda = dados.Renda.mode()

altura_moda = dados.Altura.mode()

ax = sns.displot(dados.query('Renda < 20000').Renda)
ax.figure.set_size_inches(12, 6)

ax = sns.displot(dados.Altura)
ax.figure.set_size_inches(12, 6)

quartis = dados.Renda.quantile([0.25, 0.5, 0.75])

decis = dados.Renda.quantile([i / 10 for i in range (1,10)])

percentis = dados.Renda.quantile([i / 100 for i in range (1,100)])

ax = sns.boxplot( x = 'Altura', y = 'Sexo', data = dados, orient='h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)

ax = sns.boxplot( x = 'Renda',y = 'Sexo', data = dados.query('Renda < 10000'), orient='h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Renda', fontsize=18)
ax.set_xlabel('R$', fontsize=14)

ax = sns.boxplot( x = 'Anos de Estudo', y = 'Sexo', data = dados, orient='h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Anos de Estudo', fontsize=18)
ax.set_xlabel('Anos', fontsize=14)

plt.show()