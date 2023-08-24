import pandas as pd
import json 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dados_churn = pd.read_json('Pandas\\Pandas limpeza e tratamento de dados\\data\\dataset-telecon.json')

with open('Pandas\\Pandas limpeza e tratamento de dados\\data\\dataset-telecon.json') as f:
    json_bruto = json.load(f)

dados_normalizados = pd.json_normalize(json_bruto)

idx = dados_normalizados[dados_normalizados['conta.cobranca.Total']==' '].index

dados_normalizados.loc[idx, 'conta.cobranca.Total'] = dados_normalizados.loc[idx, 'conta.cobranca.mensal'] * 24

dados_normalizados.loc[idx, 'cliente.tempo_servico'] = 24

"""print(dados_normalizados.loc[idx][
    ['cliente.tempo_servico','conta.contrato' ,'conta.cobranca.mensal','conta.cobranca.Total' ]
    ])"""

dados_normalizados['conta.cobranca.Total'] = dados_normalizados['conta.cobranca.Total'].astype('float64') 

"""for col in dados_normalizados.columns:
    print(f"Colina: {col}")
    print(dados_normalizados[col].unique())
    print("-" * 30)"""

dados_sem_vazio = dados_normalizados[dados_normalizados['Churn'] != ''].copy()

dados_sem_vazio.reset_index(drop=True, inplace=True)

dados_sem_vazio.drop_duplicates(inplace=True)

filtro_duplicadas = dados_sem_vazio.duplicated()

filtro = dados_sem_vazio['cliente.tempo_servico'].isna()

dados_sem_vazio['cliente.tempo_servico'].fillna(
    np.ceil(
        dados_sem_vazio['conta.cobranca.Total'] / dados_sem_vazio['conta.cobranca.mensal']
    ), inplace=True
)

colunas_dropar = ['conta.contrato', 'conta.faturamente_eletronico', 'conta.metodo_pagamento']

dados_sem_vazio[colunas_dropar].isna().any(axis=1).sum()

df_sem_nulos = dados_sem_vazio.dropna(subset=colunas_dropar).copy()

df_sem_nulos.reset_index(drop=True, inplace=True)

#sns.boxplot(x=df_sem_nulos['cliente.tempo_servico'])

Q1 = df_sem_nulos['cliente.tempo_servico'].quantile(.25)
Q3 = df_sem_nulos['cliente.tempo_servico'].quantile(.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_index = (df_sem_nulos['cliente.tempo_servico'] < limite_inferior) | (df_sem_nulos['cliente.tempo_servico'] > limite_superior)

df_sem_nulos[outliers_index]['cliente.tempo_servico']

df_sem_out = df_sem_nulos.copy()

df_sem_out[outliers_index]['cliente.tempo_servico']

df_sem_out.loc[outliers_index, 'cliente.tempo_servico'] = np.ceil(

        df_sem_out.loc[outliers_index,'conta.cobranca.Total'] / df_sem_out.loc[outliers_index,'conta.cobranca.mensal']
    )

#sns.boxplot(x=df_sem_out['cliente.tempo_servico'])

print(df_sem_out[outliers_index][['cliente.tempo_servico','conta.cobranca.mensal', 'conta.cobranca.Total']])

Q1 = df_sem_out['cliente.tempo_servico'].quantile(.25)
Q3 = df_sem_out['cliente.tempo_servico'].quantile(.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_index = (df_sem_out['cliente.tempo_servico'] < limite_inferior) | (df_sem_out['cliente.tempo_servico'] > limite_superior)

df_sem_out = df_sem_out[~outliers_index]

df_sem_out.reset_index(drop=True, inplace=True)

print(df_sem_out)

sns.boxplot(x=df_sem_out['cliente.tempo_servico'])
plt.show()