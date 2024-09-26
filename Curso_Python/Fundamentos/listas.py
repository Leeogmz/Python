array = []
array = list()
array_numeros = [1,2,3]
array_floats = [56.3, -2.2, 0.5]
array_str = ['A', 'B', 'C']
array_misto = [2, 2.3, 'ABC']

print(array) 
print(array_numeros) 
print(array_floats)
print(array_str)
print(array_misto)

array = list([1,2,3])
print(array)

primeiro_elemento = array[0]
print(primeiro_elemento)

array[0] = 20
primeiro_elemento = array[0]
print(primeiro_elemento)
print(array[-1])
print(array)

array = [1, 'texto', 3]

print(array[1:3])