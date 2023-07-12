import pandas as pd

dados_pacientes = pd.read_json('Pandas\Pandas-IO\data\pacientes.json')

dados_pacientes_2 = pd.read_json('Pandas\Pandas-IO\data\pacientes_2.json')

df_normalizado = pd.json_normalize(dados_pacientes_2['Pacientes'])



print(dados_pacientes.head())
print(dados_pacientes_2.head())
print(df_normalizado.head())


