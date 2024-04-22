import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Avançando em Data Science com Python\Data Visualization criando gráficos com bibliotecas Python\imigrantes_canada.csv')

df.info()

df.set_index('País', inplace = True)

anos = list (map(str, range (1980,2014)))

brasil = df.loc['Brasil', anos]

brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}

dados_brasil = pd.DataFrame(brasil_dict)

print(dados_brasil)

plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
plt.xticks(['1980','1985', '1990','1995','2000','2005','2010'])
plt.title ('Imigração do Brasil para o Canadá')
plt.xlabel('Ano')
plt.ylabel ('Número de imigrantes')
plt.show()