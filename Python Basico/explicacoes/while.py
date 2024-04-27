resposta = 'inicial'
n = 1
while  resposta != 's':
    resposta = input(f'Vamos{"s" * n} sair hoje [s/n]? ')
    n += 1
    if 'chato' in resposta or 'chata' in resposta:
        print('Foi mal')
        break
else:
    print(f'Então vamos{"s" * n}!')
