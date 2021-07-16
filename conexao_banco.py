import mysql.connector
from mysql.connector import connect, cursor

# Conexão com o banco de dados	
host = "localhost"
user = "root"
password = ""


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
cursor.execute("CREATE TABLE IF NOT EXISTS info_cadastrais(id INT AUTO_INCREMENT, Nome VARCHAR(100), Cpf VARCHAR(20), Endereço VARCHAR(100), Telefone VARCHAR(20), Email VARCHAR(100), Data_Nascimento VARCHAR(100), Idade VARCHAR(4), Sexo VARCHAR(2), primary key (id))")
print("\nTabela criada com sucesso!")

def create():
    while True:
        Nome = str(input("Digite o nome: ")).title()
        if Nome == int:
            print("Por favor, use apenas letras.")
        else:
            continue
        Cpf = str(input("Digite o CPF: "))
        Endereço = str(input("Digite o endereço: ")).title()
        Telefone = str(input("Digite o telefone: "))
        Email = str(input("Digite o e-mail: "))
        Data_Nascimento = str(input("Digite a data de nascimento [dd/mm/yyyy]: "))
        Idade = str(input("Digite a idade: "))
        Sexo = str(input("Digite o gênero: ")).capitalize()
        
        cursor.execute("INSERT INTO info_cadastrais (Nome,Cpf,Endereço,Telefone,Email,Data_Nascimento,Idade,Sexo) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(Nome,Cpf,Endereço,Telefone,Email,Data_Nascimento,Idade,Sexo))

        connection.commit()
        cursor.close()
        connection.close()

create()

