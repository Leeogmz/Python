cadastro = {'matricula': 20000168933,
            'dia_Cadastro': 25,
            'mes_cadastro': 10,
            'turma': '2E'}

print(cadastro)

print(cadastro['matricula'])

cadastro['turma'] = '2G'

print(cadastro)

cadastro ['modalidade'] = 'EAD'

print(cadastro)

cadastro.pop('turma')

print(cadastro)

cadastro.items() #retorna todos os itens do dicionario

cadastro.keys() #retorna todas as chaves do dicionario

cadastro.values() #retorna todos os valores do dicionario