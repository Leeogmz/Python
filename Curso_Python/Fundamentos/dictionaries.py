idades = {'Ana': 10, 'Maria':20, 'João':34, 'Fernando':'indefinido'}
print(idades)

nome_numeros = {7.1: 'Sete virgula um', 9.8: 'Nove virgula oito', 10.43:'Dez virgula quarenta e três'}
print(nome_numeros)

print(idades['Maria'])
print(idades['Fernando'])

print(idades.get('Fernando'))
print(nome_numeros[7.1])
print(nome_numeros.get(10.43))
print('Ana' in idades)
print('Roberto' not in idades)

idades['Maria'] = 30
idades.update({'João': 40})
print(idades)

idades['Marcos'] = 90
idades.pop('Ana')
print(idades)
idades.popitem()
print(idades)