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

media_salario = total_salario / total_empregados


print(media_salario)

professora = professora.strip().replace('y', 't').upper()

print(professora)