import numpy as np

caminho='C:\\Users\\leona\OneDrive\\Documentos\\Estudos\\Python\\Numpy\\numpy-dados\\apples_ts.csv'

print(np.loadtxt(caminho, delimiter=',', usecols=np.arange(1,88, 1)))