quantidade_seguranca = 5
salario_seguranca = 3000

quantidade_docente = 16 
salario_docente = 6000

quantidade_diretoria = 1
salario_diretoria = 12500

professora = ' Geovana Alessandra dias Sanyos '


total_empregados = quantidade_diretoria + quantidade_docente + quantidade_seguranca

total_salario = quantidade_seguranca * salario_seguranca + quantidade_docente * salario_docente + quantidade_diretoria * salario_diretoria

diferenca_salario  = salario_diretoria - salario_seguranca

media = total_salario / total_empregados


print(media)

professora = professora.strip().replace('y', 't').upper()

print(professora)

nome = input('Escreva seu nome: ')

ano_entrada = int(input('Escreva o ano de ingresso do(a) estudante: '))

print(f'Nome do aluno: {nome} - Ano de entrada: {ano_entrada}')
Le

