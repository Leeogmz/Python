import pandas as pd


dados_imdb = pd.read_xml('Pandas\Pandas-IO\data\imdb_top_1000.xml')

print(dados_imdb.head())