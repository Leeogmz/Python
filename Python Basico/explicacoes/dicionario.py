dicionario = {
    'chave' : ['valor1','valor2' ] ,
    'chave2' : ['valor3', 'valor4']
}

pessoa = {

    'nome' : 'Leonardo',
    'idade' : 26,
    'telefones' : {
        'residencial' : 99988999,
        'pessoal' : 79987987965,
        'empresarial' : 4454575784 
    }
}


nome_idade = {

    'Maria' : 50,
    'Joana' : 25
}

print(nome_idade)

nome_idade['Maria'] = 4
nome_idade['Joana'] = 20

print(nome_idade)

print(nome_idade.keys())
print(nome_idade.values())
print(pessoa.values())