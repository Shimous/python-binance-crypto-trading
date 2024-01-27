import os

from binance.client import Client
import pandas as pd

from secrets import api_secret, api_key, private_key_pass

#Conexão com api Binance
client = Client(api_key=api_key, api_secret=api_secret, private_key_pass=private_key_pass)
url = "https://api.binance.com/api/v1/sua-requisicao"
try:
    conta = client.get_account()
except:
    os.system('w32tm /resync')
finally:
    conta = client.get_account()

# Obtendo informações sobre a exchange
exchange_info = client.get_exchange_info()

# Exibindo os symbols disponíveis
#for symbol_info in exchange_info['symbols']:
#    print(symbol_info['symbol'])

lista_symbols = pd.DataFrame(exchange_info['symbols'])
lista_symbols.to_csv('lista_symbols.csv', sep=';')