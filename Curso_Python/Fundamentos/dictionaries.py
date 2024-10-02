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

idades = {'Ana': 10, 'Maria':20, 'João':34, 'Fernando':'indefinido'}

lista = idades.items()
print(lista)

for item in lista:
    print(item[0], item[1])

chaves = idades.keys()
valores = idades.values()

for item in chaves:
    print(item)

print('_________')

for item in valores:
    print(item)
lista_nome = list(idades.values())
pessoas_com_20_anos = lista_nome.count(20)
print(pessoas_com_20_anos)    
idades.clear()
print(idades)

dados_maria = {
    'sexo' : 'Feminino ',
    'cpf' : '12345678910' ,
    'rg' : '12345679' 
}
dados_joao = {
    'sexo' : 'Masculino' ,
    'cpf' : '10987654321',
    'rg' : '987654321' ,
}

dados_ana ={
    'sexo' : 'Feminino' ,
    'cpf' : '45678912310',
    'rg' : '456123789' 
}

dados_por_nome = {
    'Ana' : dados_ana,
    'Maria' : dados_maria,
    'João' : dados_joao
}

print(dados_por_nome)
print(dados_por_nome['João']['sexo'])

dados_por_nome =  {

    'Ana' : {
        'sexo' : 'Feminino' ,
        'cpf' : '45678912310',
        'rg' : '456123789' 
        } ,

    'Maria' : {
        'sexo' : 'Feminino ',
        'cpf' : '12345678910' ,
        'rg' : '12345679' 
        } ,

    'João' : {
        'sexo' : 'Masculino' ,
        'cpf' : '10987654321',
        'rg' : '987654321' ,
        }
}

print(dados_por_nome)
print(dados_por_nome['Ana']['rg'])