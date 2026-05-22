import requests
import random
from datetime import datetime
from bs4 import BeautifulSoup

def conf_sopa(url):
    #aqui é onde vamos "enganar" o mercado livre para não bloquear o robô. Esses "agentes" vão simular acessos de navegadores aleatórios,
    agentes = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    ]
    

    origens = [
        #as "origens" vão simular que o acesso veio de uma pesquisa no Google ou Bing ou  por exemplo duckduckgo. Isso ajuda a evitar bloqueios e a manter o robô funcionando por mais tempo.
        "https://www.google.com.br/",
        "https://www.bing.com/",
        "https://duckduckgo.com/",
        "https://www.google.com/",
        "https://www.google.com.br/"
    ]
    
    headers = {
         #usamos os agentes e o origens para criar um cabeçalho de requisição, que vai sortear um agente e uma origem para o mercado livre pesar que é um humano acessando o site.
        "User-Agent": random.choice(agentes),
        "Referer": random.choice(origens), 
        "Accept-Language": "en-US,en;q=0.9", #fala para o site que nós falamos inglês
        "Cache-Control": "max-age=0" , #solicita a "versão mais recente" do site, não a versão em cache
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    try:
        resposta = requests.get(url, headers=headers, timeout=15)

        if resposta.status_code == 200:
            return BeautifulSoup(resposta.text, 'html.parser')
        
        if resposta.status_code == 403:
            print("Erro 403: O site barrou o robô. Tente reiniciar a internet.")
        return None
    
    except Exception as e:
        print(f'Erro de conexão: {e}')
        return None

def minerar_links(url):
    sopa = conf_sopa(url)
    if not sopa:
        return []
    
    artistas = []

    itens = sopa.select('li.lrv-u-width-100p')

    for item in itens:
        nome_tag = item.find('h3', id='title-of-a-story')
        posicao_tag = item.find('span', class_='c-label')

        if  nome_tag:
            nome_texto = nome_tag.get_text(strip=True) 
            posicao_texto = posicao_tag.get_text(strip=True) if posicao_tag else "N/A"

            if nome_texto not in ['Songwriter', 'Producer', 'Artist']:
                artistas.append({
                    "Posição" : posicao_texto,
                    "Nome" : nome_texto,
                    "Data" : datetime.now().strftime('%d/%m/%Y')                  
                })
    return artistas
