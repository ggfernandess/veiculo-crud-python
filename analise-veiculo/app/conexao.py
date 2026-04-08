import sqlite3

def get_conn():
    conn = sqlite3.connect('veiculos.db')
    cursor = conn.cursor()
    return conn,cursor

"""
função pra criar a conexão com o banco de dados.

- sqlite3.connect('veiculos.db'): abre conexão com o banco de dados
- conn.cursor(): cria o cursor para executar comandos SQL
- return conn, cursor: retorna ambos para serem usados em outros arquivos
"""