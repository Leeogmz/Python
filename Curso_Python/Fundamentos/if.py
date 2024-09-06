#IF

print('Isto está fora dos ifs')
if (True):
    print('este codigo vai ser executado')

print('Isto está fora dos ifs')

if(False):
    print('este codigo não vai ser executado')

print('Isto está fora dos ifs')

if(True):
    pass

valor1 = 10
valor2 = 10
sao_iguais = (valor1 == valor2)
if sao_iguais: 
    print('São iguais')

valor1 = 10
valor2 = 10
if (valor1 == valor2):
    print('São iguais')
    print('São iguais, parrte 2')

valor1 = 10
valor2 = 10
if (valor1 == valor2): print('São iguais')

if (10 != 20): 
    print('São diferentes')

if ('ola' != 'alo'): 
    print('São diferentes 2')

numero = 11
if (numero>10):
    print('É maior que 10!')  

nome = input('Digite seu nome: ')     
if 'a'in nome:
    print('Esse numero possui a letra \'a\'')    

nome = input('Digite seu nome: ')  
possui_vogal = ('a' in nome) or ('o' in nome) or ('i' in nome) or ('o' in nome) or ('u' in nome)
if possui_vogal:
    print('Possui alguma vogal!')