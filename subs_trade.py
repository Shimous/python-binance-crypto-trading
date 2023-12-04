#Subrotinas do sistema
import requests

url = 'https://api.binance.com/api/v3/exchangeInfo'
response = requests.get(url)
exchange_info = response.json()

# Lista de símbolos (pares de trading)
symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]

for symbol in symbols:
    if 'BRL' in symbol:
        print(symbol)