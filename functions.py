import mysql.connector
from mysql.connector import Error


# Vai realizar a conexão com o banco de dados 
def cnn_db():
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port = '3306',
    database="exercicios"
)

def inserir_pessoa(nome, idade):

    cursor = None
    novo_id = None

    try: 
        cnn_db()
        
        cursor = conexao.cursor()

        query = "INSERT INTO pessoas (nome , idade) VALUES (%s , %s)"
        dados = (nome ,idade)

        cursor.execute(query, dados)
        conexao.commit()

        novo_id = cursor.lastrowid

        print(f"✅ Pessoa '{nome}' inserida com ID: {novo_id}")

    except Error as e:
        print(f"❌ Erro ao inserir pessoa: {e}")
        conexao.rollback()

    finally:
        if cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

    return novo_id
