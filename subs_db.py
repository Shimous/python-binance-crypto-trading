import pyodbc
from datetime import datetime

def CONNECT():
    dados_conexao = (
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=Shimote;'
        'Database=PythonTradesDB;'
        'Trusted_Connection=yes;'
        'charset=UTF-8;'
    )

    ConexaoDB = pyodbc.connect(dados_conexao)
    return ConexaoDB.cursor()

def INSERT_INTO(conexao, tabela :str, moeda: str, qtd: float, valor_reais: float,
               valor_dollar: float, saldo_reais: float, saldo_dollar: float, data_hora):
    if tabela == 'tbSaldoCarteira':
        comando = f"""INSERT INTO dbo.tbSaldoCarteira(MOEDA, QUANTIDADE, VALOR_REAIS, VALOR_DOLLAR, SALDO_REAIS, SALDO_DOLLAR, DATA)
                VALUES('{moeda}', {qtd}, {valor_reais}, {valor_dollar}, {saldo_reais}, {saldo_dollar}, '{data_hora}')"""

    conexao.execute(comando)
    conexao.commit()

