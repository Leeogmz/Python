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