
import sqlite3
import pandas as pd
import sqlalchemy 
from sqlalchemy import create_engine, MetaData, Table, inspect


engine = create_engine('sqlite:///data_base.db')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

dados = pd.read_csv(url)

#Para Criar a tabela no banco de dados
#dados.to_sql('Clientes',con=engine, index=False)

inspector = inspect(engine)


query = 'select * from Clientes where Categoria_de_renda = "Empregado"'

empregados = pd.read_sql(query, engine)

#Para Criar a tabela no banco de dados
#empregados.to_sql('Empregados',con=engine,index=False)

leitura = pd.read_sql_table('Empregados', engine)

deletando_usuario = sqlalchemy.text('DELETE FROM Clientes WHERE ID_Cliente = 5008804')
with engine.connect() as conn:
    result = conn.execute(deletando_usuario)
    conn.commit()    
    print("Registros excluídos:", result.rowcount)

