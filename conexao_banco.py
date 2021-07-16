import mysql.connector
from mysql.connector import connect, cursor

# Conexão com o banco de dados	
host = "localhost"
user = "root"
password = ""

def connection():
    try:  
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print("\nConexão estabelecida!")
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        print(err)
    
    # Criação da database e tabela
    cursor.execute("CREATE DATABASE IF NOT EXISTS dados_cadastrais")
    cursor.execute("USE dados_cadastrais")
    cursor.execute("CREATE TABLE IF NOT EXISTS info_cadastrais(id INT AUTO_INCREMENT, Nome VARCHAR(100), CPF VARCHAR(20), Endereço VARCHAR(100), Telefone VARCHAR(20), Email VARCHAR(100), Data_Nascimento VARCHAR(100), Idade VARCHAR(4), Sexo VARCHAR(2), primary key (id))")
    print("\nTabela criada com sucesso!")

connection()