import mysql.connector
from mysql.connector import connect, cursor

# PARAMETROS DE CONEXÃO
host = "localhost"
user = "root"
password = ""

# VALIDAÇÃO DA CONEXÃO COM O BD
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
    
# CRIAÇÃO DA DATABASE E TABELAS
cursor.execute("CREATE DATABASE IF NOT EXISTS dados_cadastrais")
cursor.execute("USE dados_cadastrais")
cursor.execute("CREATE TABLE IF NOT EXISTS info_cadastrais(id INT AUTO_INCREMENT, Nome VARCHAR(100), Cpf VARCHAR(20), Endereço VARCHAR(100), Telefone VARCHAR(20), Email VARCHAR(100), Data_Nascimento VARCHAR(100), Idade INT(4), Sexo VARCHAR(2), primary key (id))")

print("\nTabela criada com sucesso!")

# VALIDAÇÃO DOS CAMPOS DE INPUT
def valida_nome(Nome):
    while True:
        if not Nome.isnumeric():
            break
        else:
            print("Por favor, use apenas letras.\n")
            Nome = str(input("Digite o nome: ")).title()

def valida_cpf(Cpf):
    while True:
        if Cpf.isnumeric():
            if len(Cpf) == 11:
                break
            else:
                print("O campo de CPF deve ter ao menos 11 dígitos.\n")
                Cpf = str(input("Digite o CPF: "))
        else:
            print("No campo de CPF utilize apenas números.\n")
            Cpf = str(input("Digite o CPF: "))

def valida_telefone(Telefone):
    while True:
        if Telefone.isnumeric():
            if len(Telefone) == 11 or len(Telefone) == 10:
                break
            else:
                print("O campo de Telefone deve ter ao menos 10 dígitos.\n")
                Telefone = str(input("Digite o telefone [cod.area + numero]: "))
        else:
            print("No campo de Telefone utilize apenas números.\n")
            Telefone = str(input("Digite o telefone [cod.area + numero]: "))

def valida_email(Email):
    while True:
        if '@' in Email and '.com' in Email:
            break
        else:
            print("Revise o email por favor, e tente novamente.\n")
            Email = str(input("Digite o e-mail: ")).lower()

def valida_nascimento(Data_Nascimento):
    while True:
        if '/' in Data_Nascimento:
            if len(Data_Nascimento) == 10:
                break
            else:
                print("Por gentileza, revise a data de nascimento e utilize o padrão dd/mm/yyyy.\n")
                Data_Nascimento = str(input("Digite a data de nascimento [dd/mm/yyyy]: "))
        else:
            print("Por gentileza, revise a data de nascimento e utilize o padrão separados por '/'.\n")
            Data_Nascimento = str(input("Digite a data de nascimento [dd/mm/yyyy]: "))
      
def valida_sexo(Sexo):
    while True:
        if 'H' in Sexo or 'M' in Sexo:
            if len(Sexo) == 1:
                break
            else:
                print("Revise o sexo por favor e informe o gênero corretamente [h/m].\n")
                Sexo = str(input("Digite o gênero [h/m]: ")).title()
        else:
            print("Revise o sexo por favor e informe o gênero corretamente [h/m].\n")
            Sexo = str(input("Digite o gênero [h/m]: ")).title()


# FUNÇÃO DE CADASTRO
def cadastro():
    while True:
        Nome = str(input("\nDigite o nome: ")).title()
        valida_nome(Nome)

        Cpf = str(input("Digite o CPF: "))
        valida_cpf(Cpf)

        Endereço = str(input("Digite o endereço: ")).title()
        
        Telefone = str(input("Digite o telefone [cod.area + numero]: "))
        valida_telefone(Telefone)

        Email = str(input("Digite o e-mail: ")).lower()
        valida_email(Email)

        Data_Nascimento = str(input("Digite a data de nascimento [dd/mm/yyyy]: "))
        valida_nascimento(Data_Nascimento)

        Idade = str(input("Digite a idade: "))

        Sexo = str(input("Digite o gênero [h/m]: ")).title()
        valida_sexo(Sexo)

        # Execução do SQL com os parametros registrados nas variaveis
        cursor.execute("INSERT INTO info_cadastrais (Nome,Cpf,Endereço,Telefone,Email,Data_Nascimento,Idade,Sexo) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(Nome,Cpf,Endereço,Telefone,Email,Data_Nascimento,Idade,Sexo))

        # Commitar query e fechar conexões
        connection.commit()
        cursor.close()
        connection.close()

        print("\nDados cadastrados com sucesso!\n")
        break

cadastro()

