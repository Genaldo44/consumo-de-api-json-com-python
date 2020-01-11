import requests
import json
import pandas
url ="http://data.fixer.io/api/latest?access_key=1ef2927451be5ed3f45749f2b120d2e5"
print("Acessando base de dados do fixer.io...")
resposta = requests.get(url)
print(resposta)
if resposta.status_code == 200:
    print(" Acesso na base de dados realizado com sucesso! ")
    print(" Buscando informações... ")
    dados = resposta.json()
    print(dados)
    dolar_real = round(dados['rates']['BRL']/dados['rates'] ['USD'],2)
    euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'],2)
    bitcoin_real = round(dados['rates']['BRL'] / dados['rates']['BTC'],2)
    print(' 1 dolar vale', dolar_real, 'reais')
    print(' 1 euro vale', euro_real, 'reais')
    print(' 1 bitcoin vale', bitcoin_real, 'reais')
else:
    print("Erro ao acessar a base de dados")