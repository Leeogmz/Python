import csv
from faker import Faker
import random

fake = Faker('pt_BR')

header = ["nome", "idade", "sexo", "email", "data_nascimento", "pais", "estado", "cidade", "bairro", "salario", "cargo", "empresa", "situacao_civil", "cpf", "rg", "patrimonio"]

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
        salario = random.uniform(1000, 10000)
        cargo = fake.job()
        empresa = fake.company()
        situacao_civil = random.choice(['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)'])
        cpf = fake.cpf()
        rg = fake.rg()
        patrimonio = random.uniform(100000, 1000000)

        line = [nome, idade, sexo, email, data_nascimento, pais, estado, cidade, bairro, salario, cargo, empresa, situacao_civil, cpf, rg, patrimonio]
        writer.writerow(line)
