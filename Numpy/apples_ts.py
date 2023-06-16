import numpy as np

caminho='C:\\Users\\leona\OneDrive\\Documentos\\Estudos\\Python\\Numpy\\numpy-dados\\apples_ts.csv'
dado = np.loadtxt(caminho, delimiter=',', usecols=np.arange(1,88, 1))
#print(dado)

print(dado.ndim) #para saber as dimensões da tabela 2d
print(dado.size) #Verifica a quantidade de elemtos do array
print(dado.shape) #Verifica o numero de elementos em cada dimensão 


dado_transposto =  dado.T #para transpor os elemntos

print(dado_transposto)