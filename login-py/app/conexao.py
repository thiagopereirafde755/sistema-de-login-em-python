import mysql.connector

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="login",  
            port="3316" 
        )
        if conexao.is_connected():
            print("conexao realizada")
            return conexao
    except mysql.connector.Error as err:
        print(f"erro ao conectar: {err}")
        return None
