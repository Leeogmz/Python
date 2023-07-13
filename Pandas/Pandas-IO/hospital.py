import pandas as pd

dados_pacientes = pd.read_json('Pandas\Pandas-IO\data\pacientes.json')

dados_pacientes_2 = pd.read_json('Pandas\Pandas-IO\data\pacientes_2.json')

df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])

df_normalizado.to_json('historico_pacientes_normalizado.json')


df = pd.read_json('historico_pacientes_normalizado.json')

print(df.head())