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