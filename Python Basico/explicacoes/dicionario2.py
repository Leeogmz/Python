pessoa = {
    'nome': 'Leonardo',
    'idade': 26,
    'cpf': 78945614530,
    'telefone': {
        'residencial': 99988999,
        'pessoal': 79987987965,
        'empresarial': 4454575784
    }
}

def imprime_relatorio(pessoa):
    return f"""
    Relatório parcial
    {pessoa['nome']}, 
    portador do CPF {pessoa['cpf']}, 
    que usa o número {pessoa['telefone']['pessoal']}.
    Está oficialmente de férias.
    Ass. Direção
"""

print(imprime_relatorio(pessoa))