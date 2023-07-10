import pandas as pd

url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

dados_co2 = pd.read_excel(url)
percapita = pd.read_excel(url, sheet_name=1)
fontes = pd.read_excel(url, sheet_name=2)

intervalo = pd.read_excel(url, sheet_name=0, usecols='A:D')



#print(pd.ExcelFile(url).sheet_names)

print(dados_co2.head())
print(percapita.head())
print(fontes.head())
print(intervalo.head())