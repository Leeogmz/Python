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

dados_hospedagem[['taxa_limpeza', 'taxa_deposito', 'preco']] = dados_hospedagem[['taxa_limpeza', 'taxa_deposito', 'preco']].applymap(lambda x: x.replace('$','').replace(',','').strip())

col_valores = ['taxa_limpeza', 'taxa_deposito', 'preco']

dados_hospedagem[col_valores] = dados_hospedagem[col_valores].astype(np.float64)

dados_hospedagem['descricao_local'] = dados_hospedagem['descricao_local'].str.lower()

dados_hospedagem['descricao_local']=dados_hospedagem['descricao_local'].str.replace('[^a-zA-Z0-9\-\']',' ', regex=True)

dados_hospedagem['descricao_local']=dados_hospedagem['descricao_local'].str.replace('(?<!\w)-(?!\w)',' ', regex=True)


print(dados_hospedagem['descricao_local'][3169])


#print(dados_hospedagem.info())

#print(dados_hospedagem)