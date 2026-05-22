import requests
import pandas as pd
from datetime import datetime
import time
import os
from tools import minerar_links

print("RASTREADOR DE POP STAR EM ALTA NO MOMENTO!")

url = "https://www.billboard.com/charts/artist-100/"

listas_artistas = minerar_links(url)

c=0
if listas_artistas[:10]:
    for a in listas_artistas:
        print(f"{c}º - {a['Nome']}")
        c = c + 1

    df = pd.DataFrame(listas_artistas)
    arquivo_existe = os.path.exists('historico_billboard.csv')
    df.to_csv('historico_billboard.csv', mode='a', header=not arquivo_existe, encoding='utf-8-sig')
else: 
    print('Nenhum artista enconrado.')                                                     

