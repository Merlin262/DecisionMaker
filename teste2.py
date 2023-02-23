import pandas as pd
import random


movies_df = pd.read_table("data/data.tsv", low_memory=False)
filtro_df = movies_df.loc[movies_df['titleType']!='tvEpisode']


print("Menu")
categoria=int(input("Escolha dentre as categorias a seguir: \n 1 - Priorizar tipo de filme\n 2 - Priorizar gênero\n 3 - Priorizar classificação indicativa\n 4 - Ano de lançamento\n Opção desejada: "))


if categoria==1:
    tipo=(input("Escreva 'short' para curta e 'movie' para filmes e 'tvSeries': "))
    print(filtro_df[filtro_df['titleType'] == tipo].sample())

elif categoria==2:
    gen=input("Informe o gênero desejado (exemplo: 'Animation; Comedy; Drama...'): ")
    print(filtro_df[filtro_df['genres'] == gen].sample())

elif categoria==3:
    opc=input("Informe se deseja uma mídia para maiores de idade('-18' ou '+18'): ")
    if opc == '-18':
        print(filtro_df[filtro_df['isAdult'] == '0'].sample())
    elif opc == '+18':
        print(filtro_df[filtro_df['isAdult'] == '1'].sample())
    else:
        print("Informe um valor válido")    
        
elif categoria==4:
    ano=input("Informe o Ano desejado: ")
    print(filtro_df[filtro_df['startYear'] == ano].sample())
