import pandas as pd

caminho = 'C:\\Users\\leona\\OneDrive\\Documentos\\Estudos\\Python\\Pandas\\Pandas seleção e agrupamento de dados\\data\\1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

emissoes_gases = pd.read_excel(caminho, sheet_name='GEE Estados')

#print(emissoes_gases.head())

print(emissoes_gases.info())