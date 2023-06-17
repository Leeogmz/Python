import numpy as np
import matplotlib.pyplot as plt

caminho='C:\\Users\\leona\OneDrive\\Documentos\\Estudos\\Python\\Numpy\\numpy-dados\\apples_ts.csv'
dado = np.loadtxt(caminho, delimiter=',', usecols=np.arange(1,88, 1))
#print(dado)

#print(dado.ndim) #para saber as dimensões da tabela 2d
#print(dado.size) #Verifica a quantidade de elemtos do array
#print(dado.shape) #Verifica o numero de elementos em cada dimensão 


dado_transposto =  dado.T #para transpor os elemntos

datas = dado_transposto[:,0] #para separar a primeira coluna
datas = np.arange(1,88, 1)
precos = dado_transposto [:,1:6]


Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]


grafico = plt.plot(datas, Kaliningrad)
plt.show()

