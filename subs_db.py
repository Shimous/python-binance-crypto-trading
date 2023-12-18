import pyodbc
import pandas as pd

def CONNECT():
    dados_conexao = (
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=Shimote;'
        'Database=PythonTradesDB;'
        'Trusted_Connection=yes;'
        'charset=UTF-8;'
    )

    ConexaoDB = pyodbc.connect(dados_conexao)
    return ConexaoDB

def INSERT_INTO(conexao, tabela:str, moeda:str, qtd:float, valor_reais:float, valor_dollar:float, **kwargs):

    if tabela == 'tbSaldoCarteira':
        # Extração kwargs para tabela tbSaldoCarteira
        saldo_reais = kwargs['saldo_reais']
        saldo_dollar = kwargs['saldo_dollar']
        data_hora = kwargs['data_hora']

        comando = f"""INSERT INTO dbo.tbSaldoCarteira(MOEDA, QUANTIDADE, VALOR_REAIS, VALOR_DOLLAR, SALDO_REAIS, SALDO_DOLLAR, DATA)
                VALUES('{moeda}', {qtd}, {valor_reais}, {valor_dollar}, {saldo_reais}, {saldo_dollar}, '{data_hora}')"""

    elif tabela == 'tbOrdens':
        # Extração kwargs para tabela tbOrdens
        id_binance = kwargs['id_binance']
        operacao = kwargs['operacao']
        data_pedido = kwargs['data_pedido']
        if kwargs['data_execucao'] != None:
            data_execucao = kwargs['data_execucao']
            comando = f"""INSERT INTO dbo.tbOrdens(ID_BINANCE, MOEDA, QUANTIDADE, PRECO_REAL, PRECO_DOLLAR, OPERACAO, DATA_PEDIDO, DATA_EXECUCAO)
                                        VALUES('{id_binance}', '{moeda}', {qtd}, {valor_reais}, {valor_dollar},{operacao}, {data_pedido}, '{data_execucao}')"""
        else:
            data_execucao = 'NULL'
            comando = f"""INSERT INTO dbo.tbOrdens(ID_BINANCE, MOEDA, QUANTIDADE, PRECO_REAL, PRECO_DOLLAR, OPERACAO, DATA_PEDIDO, DATA_EXECUCAO)
                        VALUES('{id_binance}', '{moeda}', {qtd}, {valor_reais}, {valor_dollar}, '{operacao}', {data_pedido}, {data_execucao})"""



    conexao.cursor().execute(comando)
    conexao.commit()

def SELECT(conexao, tabela:str) -> pd.DataFrame:
    comando = f'SELECT * FROM dbo.{tabela}'
    return pd.read_sql(sql=comando, con=conexao)

if __name__ == '__main__':
    conexao = CONNECT()
    print(SELECT(conexao, tabela='tbSaldoCarteira'))
