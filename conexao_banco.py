import mysql.connector
from mysql.connector import connect, cursor

# Conexão com o banco de dados	
host = "localhost"
user = "root"
password = ""

# Validação da conexão com o banco de dados
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

# Função de cadastro de novo usuário
def cadastro():
    while True:
        while True:
            Nome = str(input("\nDigite o nome: ")).title()
            if not Nome.isnumeric():
                break
            else:
                print("Por favor, use apenas letras.\n")
        while True:
            Cpf = str(input("Digite o CPF: "))
            if Cpf.isnumeric():
                break
            else:
                print("Utilize apenas números.\n")
        Endereço = str(input("Digite o endereço: ")).title()
        while True:
            Telefone = str(input("Digite o telefone: "))
            if Telefone.isnumeric():
                break
            else:
                print("Utilize apenas números.\n")
        while True:
            Email = str(input("Digite o e-mail: "))
            if '@' in Email and '.com' in Email:
                break
            else:
                print("Revise o email por favor, e tente novamente.\n")
        while True:
            Data_Nascimento = str(input("Digite a data de nascimento [dd/mm/yyyy]: "))
            if '/' in Data_Nascimento:
                break
            else:
                print("Por gentileza, revise a data de nascimento e utilize o padrão dd/mm/yyyy separados por '/'.\n")
        while True:
                Idade = str(input("Digite a idade: "))
                if Idade.isnumeric():
                    break
                else:
                    print("Utilize apenas números.\n")
        while True:
            Sexo = str(input("Digite o gênero [h/m]: ")).title()
            if 'H' in Sexo or 'M' in Sexo:
                break
            else:
                print("Informe o gênero corretamente [h/m].\n")

        # Execução do SQL com os parametros registrados nas variaveis
        cursor.execute("INSERT INTO info_cadastrais (Nome,Cpf,Endereço,Telefone,Email,Data_Nascimento,Idade,Sexo) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(Nome,Cpf,Endereço,Telefone,Email,Data_Nascimento,Idade,Sexo))

        # Commitar query e fechar conexões
        connection.commit()
        cursor.close()
        connection.close()

        print("\nDados cadastrados com sucesso!\n")
        break

create()

