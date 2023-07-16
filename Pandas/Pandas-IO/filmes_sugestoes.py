import pandas as pd

dados_html = pd.read_html('C:\\Users\\leona\OneDrive\\Documentos\\Estudos\\Python\\Pandas\\Pandas-IO\\data\\filmes_wikipedia.html')

top_filmes = dados_html[1]

top_filmes.to_html('top_filmes.html')

print(top_filmes)