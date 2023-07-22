import pandas as pd

caminho = 'C:\\Users\\leona\\OneDrive\\Documentos\\Estudos\\Python\\Pandas\\Pandas seleção e agrupamento de dados\\data\\1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

emissoes_gases = pd.read_excel(caminho, sheet_name='GEE Estados')

#print(emissoes_gases['Emissão / Remoção / Bunker'].unique())

#print((emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção')) 

#emissoes_gases_remocao = emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI','Remoção']), 1970:2021].max()

emissoes_gases_bunker = emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

emissoes_gases_final = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases_final = emissoes_gases.drop(columns= 'Emissão / Remoção / Bunker')



print(emissoes_gases_final)