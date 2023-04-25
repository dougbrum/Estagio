import pandas as pd
df = pd.read_csv('actors.csv')

#1Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

df['Actor'][df['Number of Movies'] == df['Number of Movies'].max()]

# 2Apresente a média da coluna contendo o número de filmes.
df['Number of Movies'].mean()

# 3 Apresente o nome do ator/atriz com a maior média por filme.

df['Actor'][df['Average per Movie'] == df['Average per Movie'].max()]

# 4 Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

df['#1 Movie'].value_counts().head(1)