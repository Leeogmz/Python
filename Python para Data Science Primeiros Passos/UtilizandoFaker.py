import csv
from faker import Faker
import random
from lentes import lentes_oculos  # Importa a lista de lentes de óculos do arquivo lentes.py

fake = Faker('pt_BR')

header = ["nome", "idade", "sexo", "email", "data_nascimento", "pais", "estado", "cidade", "bairro", "salario", "cargo", "empresa", "situacao_civil", "cpf", "rg", "patrimonio", "produto_comprado", "valor_produto"]



with open("dados.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    for _ in range(100000):
        nome = fake.name()
        idade = random.randint(18, 80)
        sexo = random.choice(['M', 'F'])
        email = fake.email()
        data_nascimento = fake.date_of_birth().strftime('%d/%m/%Y')
        pais = fake.country()
        estado = fake.state()
        cidade = fake.city()
        bairro = fake.neighborhood()
        salario = random.uniform(1320, 13200)
        cargo = fake.job()
        empresa = fake.company()
        situacao_civil = random.choice(['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)'])
        cpf = fake.cpf()
        rg = fake.rg()
        patrimonio = random.uniform(100000, 1000000)
        produto_comprado = random.choice(lentes_oculos)  # Seleciona um nome de lente de óculos aleatoriamente
        valor_produto = random.uniform(1000, 7000)

        line = [nome, idade, sexo, email, data_nascimento, pais, estado, cidade, bairro, salario, cargo, empresa, situacao_civil, cpf, rg, patrimonio, produto_comprado, valor_produto]
        writer.writerow(line)

        #print(line)
