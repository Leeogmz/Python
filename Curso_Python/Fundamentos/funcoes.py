def func():
    num = 10
    print('Uma função %d' % (num))
func()    

def func():
    pass
func()

def print_var (numero):
    print(numero)

print_var(2)    
print('Maça')

def print_soma(num1,num2):
    print(num1+num2)

print_soma(50,50)    
print_soma(25.5,24.5)  
print_soma('Olá ', 'mundo')

def func(*args):
    print(type(args))
    print('Argumentos são: ', args)

func(1,2,3)
func()
func('Olá', True, [1,2,3])

def print_sub(num1,num2):
    print(num1-num2)

print_sub(10,2)  
print_sub(num2=2,num1=10)      

def func(*args, outro):
    print('Argumentos são: ', args)
    print(outro)

func(1,2,3, outro=1)
func(outro=2)        
func('Olá', True, [1,2,3], outro=3)


def func(valor, nome = 'Teste'):
    print(nome, valor)

func(3)  
func(3, 'Leonardo')  

def func (**args):
    print(type(args))
    print(args)
    print(args['valor'])

func( valor = 10, operacao = 'soma', resultado = 10 )

def printa(x):
    print(x)

def executa_func(func, x):
    func(x)

minha_funcao = printa
print(type(minha_funcao))

executa_func(minha_funcao, 10)

def subtrai(num1,num2):
    valor = num1 - num2
    return valor
subtracao = subtrai(10,3)
print(subtracao)

def len_int(numero):
    numero_em_texto = str(numero)
    return len(numero_em_texto)
num1 = 10
num2 = 1230

tamanho1= len_int(num1)
tamanho2= len_int(num2)

print('O número %d tem %d dígitos' % (num1, tamanho1))
print('O número %d tem %d dígitos' % (num2, tamanho2))

def retorna_multiplo():
    return 1,2
valor = retorna_multiplo()
print(valor)
print(type(valor))

def retorna_multiplo(a,b,c):
    a+=a
    b+=b
    c+=c
    return a,b,c

x,y,z = retorna_multiplo(1,2,3)
print(x,y,z)

a = retorna_multiplo(1,2,3)
print(a)

def func():
    print('Olá')
    return
    print('123')

func()    

def func(x):
    if x == 'Olá':
        print('Olá')
        return
    print('123')
    return x

func('x')  

faz_soma = lambda x : x + 10
valor = faz_soma(2)
print(valor)

multiplica = lambda x,y : x * y
valor = multiplica(2,10)
print(valor)

def multiplica(y):
    return lambda x : x * y

valor = multiplica(2)    
resultado = valor(20)
print(resultado)

def print_num (num):
    print(num)
    if num >= 10:
        return
    print_num(num+1)

print_num(0)

def print_str(texto, indice):
    if indice == len(texto):
        return
    print(texto[indice])
    print_str(texto, indice + 1)
print_str('python', 0)

def fatorial(num):
    if num == 1:
        return 1
    return num * fatorial(num-1)
print(fatorial(5))