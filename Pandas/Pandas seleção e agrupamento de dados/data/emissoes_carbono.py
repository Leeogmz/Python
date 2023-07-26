import pandas as pd
import matplotlib.pyplot as plt


caminho = 'C:\\Users\\leona\\OneDrive\\Documentos\\Estudos\\Python\\Pandas\\Pandas seleção e agrupamento de dados\\data\\1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

emissoes_gases = pd.read_excel(caminho, sheet_name='GEE Estados')

emissoes_gases_final = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases_final = emissoes_gases.drop(columns= 'Emissão / Remoção / Bunker')


colunas_info = list(emissoes_gases_final.loc[:,'Nível 1 - Setor' : 'Produto'].columns)

colunas_emissao = list(emissoes_gases_final.loc[:,1970:2021].columns)

emissoes_por_ano = emissoes_gases_final.melt(id_vars = colunas_info, value_vars=colunas_emissao, var_name='Ano', value_name='Emissao')



#Para agrupar os gases (cria um dicionario com os gases separados ao adicionar o .groups
emissoes_por_ano_agrupadas = emissoes_por_ano.groupby('Gás').groups
#Para filtrar apenas um gás especifico
#emissoes_por_ano_agrupadas = emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

emissoes_por_gas_soma = emissoes_por_ano.groupby('Gás')[['Emissao']].sum().sort_values('Emissao', ascending=False)

emissoes_por_gas_soma.plot(kind= 'barh', figsize= (10,6));
#plt.show()

print(f'A emissão de Co2 corresponde a {float((emissoes_por_gas_soma.iloc[0:9].sum()/emissoes_por_gas_soma.sum()).iloc[0])*100:.2f} % de emissão total de gases estufa no Brasil de 1970 a 2021. ')

gas_por_setor = emissoes_por_ano.groupby(['Gás', 'Nível 1 - Setor'])[['Emissao']].sum()

co2_por_setor = gas_por_setor.xs('CO2 (t)', level = 0).idxmax()

print(co2_por_setor)