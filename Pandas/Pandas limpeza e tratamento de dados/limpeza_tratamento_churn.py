import pandas as pd
import json 

dados_churn = pd.read_json('Pandas\\Pandas limpeza e tratamento de dados\\data\\dataset-telecon.json')

with open('Pandas\\Pandas limpeza e tratamento de dados\\data\\dataset-telecon.json') as f:
    json_bruto = json.load(f)

dados_normalizados = pd.json_normalize(json_bruto)

dados_normalizados['conta.contrato'][2075] = 'dois anos'

idx = dados_normalizados[dados_normalizados['conta.cobranca.Total']==' '].index

dados_normalizados.loc[idx, 'conta.cobranca.Total'] = dados_normalizados.loc[idx, 'conta.cobranca.mensal'] * 24

dados_normalizados.loc[idx, 'cliente.tempo_servico'] = 24

print(dados_normalizados.loc[idx][
    ['cliente.tempo_servico','conta.contrato' ,'conta.cobranca.mensal','conta.cobranca.Total' ]
    ])

dados_normalizados['conta.cobranca.Total'] = dados_normalizados['conta.cobranca.Total'].astype('float64') 

dados_normalizados.info()

print(dados_normalizados.head())