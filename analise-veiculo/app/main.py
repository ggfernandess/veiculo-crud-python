from conexao import get_conn

def listar():
    conn, cursor = get_conn()
    cursor.execute("SELECT * FROM veiculos")

    for linha in cursor.fetchall():
        print(linha)
    
    conn.close()

def inserir():
    conn,cursor = get_conn()

    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    preco = float(input("preco: "))

    cursor.execute("""
    INSERT INTO veiculos (marca, modelo, ano, preco)
    VALUES (?,?,?,?)""",(marca,modelo,ano,preco))

    conn.commit()
    conn.close()

    print("Veiculo foi cadastrado.")

def atualizar():
    conn,cursor = get_conn()

    id_veiculo = int(input("Qual a ID do veiculo?"))
    novo_preco = float(input("Qual o novo preco do veiculo?"))

    cursor.execute(""" UPDATE veiculos
                   SET preco = ?
                   WHERE id = ?
    """, (novo_preco, id_veiculo))

    conn.commit()
    conn.close()

    print("Atualizado!")

def deletar():
    conn,cursor = get_conn()

    id_veiculo = int(input("Qual a ID do veiculo que deseja deletar?:"))
    
    cursor.execute("DELETE FROM veiculos WHERE id = ?", (id_veiculo,))

    conn.commit()
    conn.close()

    print("Deletado!")
    
while True:
    print("\n1 - Listar veiculos")
    print("2- Inserir")
    print("3- Atualizar")
    print("4- Deletar")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar()
    elif opcao == "2":
        inserir()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        deletar()
    elif opcao == "5":
        break
    else:
        print("Opção invalida!")

"""""
No codigo principal, foi feito as funções que se comunicam
com o SQL. 
Logo após, foi feito um menu interativo, onde o usuário pode 
utilizar o sistema.
"""