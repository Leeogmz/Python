import requests
import json
import pandas as pd


dados_frutas = requests.get('https://fruityvice.com/api/fruit/all')
resultado = json.loads(dados_frutas.text)

dados_frutas_normalizado = pd.json_normalize(resultado)

print(dados_frutas_normalizado.head())