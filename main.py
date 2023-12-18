#by Pedro Shimote (Shimous)

#https://pypi.org/project/python-binance/
#https://python-binance.readthedocs.io/en/latest/overview.html


from secrets import api_secret, api_key, private_key_pass
from subs_db import CONNECT, INSERT_INTO

from binance.client import Client
from datetime import datetime
import os

#Conexão com api Binance------------------------------------------------------------------------------------------------
client = Client(api_key=api_key, api_secret=api_secret, private_key_pass=private_key_pass)
url = "https://api.binance.com/api/v1/sua-requisicao"
try:
    conta = client.get_account()
except:
    os.system('w32tm /resync')
finally:
    conta = client.get_account()

saldo_total_reais = 0
saldo_total_dollar = 0
conexaoDB = CONNECT()

#Gravação das cotações dos ativos com saldo > 0, no DB
for asset in conta['balances']:
    moeda = asset['asset']
    quantidade = float(asset['free'])
    if float(quantidade) > 0:
        symbol_reais = f'{moeda}BRL'
        symbol_dollar = f'{moeda}FDUSD'
        cotacao_reais = float(client.get_recent_trades(symbol=symbol_reais, limit=1)[0]['price'])
        try:
            cotacao_dollar = float(client.get_recent_trades(symbol=symbol_dollar, limit=1)[0]['price'])
        except:
            symbol_dollar = f'FDUSD{moeda}'
            cotacao_dollar = float(client.get_recent_trades(symbol=symbol_dollar, limit=1)[0]['price'])
        data_hora_requisicao = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        saldo_reais = cotacao_reais * quantidade
        saldo_dollar = cotacao_dollar * quantidade

        print(f'{moeda}: qtd = {quantidade}, Cotação atual R$ = {cotacao_reais}, Cotação atual $ = {cotacao_dollar} ')
        print(f'----> Saldo R$: {round(saldo_reais, 2)}, Saldo $: {round(saldo_dollar, 2)}')
        INSERT_INTO(conexaoDB, 'tbSaldoCarteira', moeda, quantidade, cotacao_reais, cotacao_dollar, saldo_reais=saldo_reais, saldo_dollar=saldo_dollar, data_hora=data_hora_requisicao)

        saldo_total_reais = saldo_total_reais + saldo_reais
        saldo_total_dollar = saldo_total_dollar + saldo_dollar

print('==================================================')
print(f'Saldo total R$: {round(saldo_total_reais,2)}, Saldo total $: {round(saldo_total_dollar, 2)}')
cotacao_dollar_real = float(client.get_recent_trades(symbol='USDTBRL', limit=1)[0]['price'])
print(f'Cotação do Dollar: R${round(cotacao_dollar_real,2)}')

#丂んﾉﾶのひ丂

