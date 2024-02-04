import os

from binance.client import Client
import pandas as pd

from secrets import api_secret, api_key, private_key_pass

#Salva informações de moedas e de trades
def GetExchangeInfo():
    client = Client(api_key=api_key, api_secret=api_secret, private_key_pass=private_key_pass)
    try:
        exchange_info = client.get_exchange_info()
    except:
        os.system('w32tm /resync')
    finally:
        exchange_info = client.get_exchange_info()

    # Obtendo informações sobre a exchange
    exchange_info = client.get_exchange_info()

    lista_symbols = pd.DataFrame(exchange_info['symbols'])
    lista_filters = pd.json_normalize(lista_symbols['filters'])
    lista_symbols = pd.merge(lista_symbols, lista_filters, how='inner', left_index=True, right_index=True)

    lista_symbols.to_csv('lista_symbols.csv', sep=';')

if __name__ == '__main__':
    GetExchangeInfo()