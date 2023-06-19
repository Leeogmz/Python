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




Moscow_ano1 = Moscow[0:12]
Moscow_ano2= Moscow[13:25]
Moscow_ano3 = Moscow[25:37]
Moscow_ano4 = Moscow[37:49]

plt.plot(np.arange(1,13,1) , Moscow_ano1)
plt.plot(np.arange(1,13,1) , Moscow_ano2)
plt.plot(np.arange(1,13,1) , Moscow_ano3)
plt.plot(np.arange(1,13,1) , Moscow_ano4)
plt.legend(['Ano1','Ano2','Ano3','Ano4', ])
plt.show()

#print(np.array_equal(Moscow_ano3, Moscow_ano4))

#print(np.allclose(Moscow_ano3, Moscow_ano4,10))



#print(sum(np.isnan(Kaliningrad))) #Retorna a quantidade de Nan 

#(Kaliningrad[3] + Kaliningrad[5]) / 2
Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]])

grafico = plt.plot(datas, Kaliningrad)
plt.show()