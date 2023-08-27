import pandas as pd
import numpy as np
import seaborn as sns
import scipy
import matplotlib.pyplot as plt


dados = pd.read_csv('C:\\Users\\leona\\OneDrive\\Documentos\\Estudos\\Python\\Estatística com Python\Frequências e medidas\\dados.csv')


print(dados.head())
dados.info()

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

print(frequencia)
print(percentual)
print(dist_freq_qualitativas)