#NÃO FUNCIONA 
""" 
def func():
    variavel_local = 10

func()
print(variavel_local)   
"""

#FUNCIONA
var2 = 10
def func():
    print(var2)
    variavel_local = 10
func()
print('--------------')

var2 = 10
if True:
    var2 = 20
print(var2)
print('--------------')

var2 = 10

def func():
    var2 = 20
    print(var2)
func()
print(var2)
print('--------------')

var2 = 10

def func():
    global var2
    var2 = 20

func()
print(var2)
print('--------------')


def func_pai():
    pai = 10
    def func_filho():
        print(pai)
    func_filho()

func_pai()
print('--------------')


def func_pai():
    pai = 10
    def func_filho():
        pai =20
        print(pai)
    func_filho()
    print(pai)

func_pai()
print('--------------')


def func_pai():
    pai = 10
    def func_filho():
        nonlocal pai 
        pai = 20
        print(pai)
    func_filho()
    print(pai)

func_pai()
print('--------------')

var = 20
print(var)
del var
#print(var) NameError: name 'var' is not defined.

array = [1,2,3]
del array[0]
print(array)

array = [1,2,3]
del array[:2]
print(array)