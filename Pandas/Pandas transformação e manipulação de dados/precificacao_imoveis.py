import pandas as pd 
import numpy as np

dados_hospedagem = pd.read_json('Pandas\\Pandas transformação e manipulação de dados\\data\\dados_hospedagem.json')

dados_hospedagem = pd.json_normalize(dados_hospedagem['info_moveis'])

colunas = list(dados_hospedagem.columns)

dados_hospedagem = dados_hospedagem.explode(colunas[3:])

dados_hospedagem.reset_index(inplace=True, drop=True)

col_numericas = ['quantidade_banheiros', 'quantidade_quartos', 'quantidade_camas', 'max_hospedes']

dados_hospedagem[col_numericas] = dados_hospedagem[col_numericas].astype(np.int64)

dados_hospedagem['avaliacao_geral'] = dados_hospedagem['avaliacao_geral'].astype(np.float64)

print(dados_hospedagem.info())

print(dados_hospedagem)