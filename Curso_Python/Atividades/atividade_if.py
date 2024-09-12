#1° 

saldo_bancario = float(input('Digite seu saldo bancario: '))
saldo_divida = float(input('Digite quanto você deve: '))
resultado = saldo_bancario - saldo_divida

if resultado >= 0:
    print('Seu saldo é positivo.')
else:
    print('Seu saldo é negativo. ')

#2°

cpf = '999.999.999-99' 
senha = '1234'
senha_input = input('Digite sua senha: ')

if senha_input == senha:
    print(cpf)
else: 
    print('Senha incorreta! ')

#3° 

idade = int(input('Digite sua idade: '))
 
if idade <= 3:
   print('Você ainda é um bebe')
elif idade <= 13:
    print('Você é uma criança')
elif idade <= 18:
    print('Você é um adolescente')
elif idade <= 65:
    print('Você é um adulto')
else: 
    print('Você é um idoso')  
    

#4°

nume1 = float(input('Digite o primeiro número: '))
nume2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação: ')    

if (operacao == "+"):
    soma = nume1 + nume2
    print("A soma é: ", soma) 
elif (operacao == "-"):
    subtracao = nume1 - nume2
    print("A subtração é ", subtracao) 
elif (operacao == "*") :
    multiplicacao = nume1 * nume2
    print("A multiplição é ", multiplicacao) 
elif (operacao == "/"): 
    divisao = nume1 / nume2
    print("A divisão é ", divisao)
else:
    print("Operação Inválida!")