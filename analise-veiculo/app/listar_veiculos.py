from conexao import get_conn

conn,cursor = get_conn()

cursor.execute("SELECT * FROM veiculos")
dados = cursor.fetchall()

for linha in dados:
    print(linha)

conn.close()

"""
Conecta ao banco SQLite, busca todos os veículos e imprime os resultados.
"""