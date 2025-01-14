import mysql.connector

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost", 
            user="root", #usuario
            password="",  #senha
            database="lista_tarefa",  #database
            port="3316" #porta
        )
        if conexao.is_connected():
            print("conexao realizada")
            return conexao
    except mysql.connector.Error as err:
        print(f"erro ao conectar: {err}")
        return None
