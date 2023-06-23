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

""" plt.plot(np.arange(1,13,1) , Moscow_ano1)
plt.plot(np.arange(1,13,1) , Moscow_ano2)
plt.plot(np.arange(1,13,1) , Moscow_ano3)
plt.plot(np.arange(1,13,1) , Moscow_ano4)
plt.legend(['Ano1','Ano2','Ano3','Ano4', ])
plt.show() """

#print(np.array_equal(Moscow_ano3, Moscow_ano4))

#print(np.allclose(Moscow_ano3, Moscow_ano4,10))



#print(sum(np.isnan(Kaliningrad))) #Retorna a quantidade de Nan 

#(Kaliningrad[3] + Kaliningrad[5]) / 2
Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]])

""" grafico = plt.plot(datas, Kaliningrad)
plt.show() """



x = datas

y = 0.52*x+80

plt.plot(datas, Moscow)
plt.plot(x, y)
plt.show()

#np.sqrt(np.sum(np.power(Moscow - y, 2))) ou np.linalg.norm(Moscow-y)

print(np.sqrt(np.sum(np.power(Moscow - y, 2))))




""" A equação de uma reta na forma y = ax + b é uma expressão matemática que descreve a relação entre os valores de x e y em uma linha reta. O valor de "a" representa a inclinação (ou declive) da reta, que é a taxa de variação entre os valores de x e y. O valor de "b" é o ponto de intercepção no eixo y, ou seja, o valor de y quando x é igual a zero. Com essa equação, é possível plotar a reta em um sistema de coordenadas cartesianas, onde o eixo x representa os valores de x e o eixo y representa os valores de y. A equação da reta é amplamente utilizada em várias áreas da matemática e também em outras áreas, como física e engenharia, para modelar dados e prever comportamentos futuros.
"""

"""
O coefiente angular pode ser obtido usando a equação:

a = n*Soma( Xi*Yi ) - Soma( Xi )*Soma(Yi) / nSoma(Xi^2) - (Soma(Xi))^2 


Coeficiente linear 

b = Media(Yi) - a * Media(Xi) 

"""


n = np.size(Moscow) #número de elementos

Y = Moscow

X = datas

a = (n*np.sum(X*Y) - np.sum(X) * np.sum(Y)) / (n*np.sum(X**2) - np.sum(X)**2) #Coeficiente angular

b = b = np.mean(Y) - a*np.mean(X)

y = a*X+b

print(np.linalg.norm(Moscow-y))



plt.plot(x, Moscow)
plt.plot(41.5,41.5*a+b, '*r')
plt.plot(100,100*a+b, '*r')
plt.show()

#print(np.random.randint(low=40,high=100,size=100))
coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)


norma = np.array([])

for i in range (100):
  norma = np.append(norma, np.linalg.norm(Moscow-(coef_angulares[i]*X+b)))


print(norma)  

print(coef_angulares[1])

