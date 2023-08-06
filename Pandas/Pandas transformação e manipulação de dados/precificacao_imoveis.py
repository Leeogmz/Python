import pandas as pd 

dados_hospedagem = pd.read_json('Pandas\\Pandas transformação e manipulação de dados\\data\\dados_hospedagem.json')

dados_hospedagem = pd.json_normalize(dados_hospedagem['info_moveis'])

colunas = list(dados_hospedagem.columns)

dados_hospedagem = dados_hospedagem.explode(colunas[3:])

dados_hospedagem.reset_index(inplace=True, drop=True)

print(dados_hospedagem)