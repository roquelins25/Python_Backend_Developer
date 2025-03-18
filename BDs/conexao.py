import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela ( conexao,cursor):
    cursor.execute("CREATE TABLE clientes (ID INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100),email VARCHAR(30))" )

def inserir_registro(conexao,cursor,nome,email):
    data = (nome,email)
    cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?);" ,data)
    conexao.commit()

def Atualizar_registro(conexao,cursor,nome,email,id):
    data = (nome,email,id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE ID=? ;" ,data)
    conexao.commit()

def Deletar_registro(conexao,cursor,id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE ID=? ;" ,data)
    conexao.commit()

def Inserir_Lote(conexao,cursor,dados):
    cursor.executemany("INSERT INTO clientes (nome,email) VALUES (?,?);" ,dados)
    conexao.commit()

def Select_dados(cursor,coluna,id):
    cursor.execute("SELECT * FROM clientes WHERE ?=?", (coluna,id))
    return cursor.fetchone()

cliente = Select_dados(cursor,'nome',"RoqueLins")
print(cliente)