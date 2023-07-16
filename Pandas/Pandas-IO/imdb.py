import pandas as pd


dados_imdb = pd.read_xml('Pandas\Pandas-IO\data\imdb_top_1000.xml')

dados_imdb.to_xml('filmes_imdb.xml')

print(dados_imdb.head())