import requests
import pandas as pd
from datetime import datetime
import time
import os
from tools import minerar_links

print("RASTREADOR DE POP STAR EM ALTA NO MOMENTO!")

url = "https://www.billboard.com/charts/artist-100/"

listas_artistas = minerar_links(url)


if listas_artistas[:10]:
    for a in listas_artistas:
        print(f"{listas_artistas}º - {a['Nome']}")

    df = pd.DataFrame(listas_artistas)
    df.index = df.index + 1
    arquivo_existe = os.path.exists('historico_billboard.csv')
    df.to_csv('historico_billboard.csv', mode='a', header=not arquivo_existe, encoding='utf-8-sig')
else: 
    print('Nenhum artista enconrado.')                                                     

