# 1°

falta_comida = False
e_sabado = True
print("Devo ir ao mercado", falta_comida or e_sabado)

#2° 

sinal_vermelho = True
carro_vindo_direita = False
carro_vindo_esquerda = True
print("Posso atravessar a rua? ", (sinal_vermelho and (not carro_vindo_direita and not carro_vindo_esquerda)))

#3° 

sinal_vermelho = True
carro_vindo_direita = False
carro_vindo_esquerda = False
print("Posso atravessar a rua? ", (sinal_vermelho or (not carro_vindo_direita and not carro_vindo_esquerda)))
