# Crie um código em Python que teste se o site Pudim está acessível pelo computador
import requests

# Variável contendo o site
site = 'https://www.pudim.com.br/'

# Verificando se o site está online
try:
    resposta = requests.get(site)
    if resposta.status_code == 200:
        print(f"O site {site} está online")
except Exception as erro:
    print("O site está offline")
    print(f"Erro encontrado: \n{erro}")
