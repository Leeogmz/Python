import pandas as pd
import sqlalchemy 
from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

dados = pd.read_csv(url)

dados.to_sql('Clientes', index=False)

inspector = inspect(engine)

print(inspector.get_table_names())