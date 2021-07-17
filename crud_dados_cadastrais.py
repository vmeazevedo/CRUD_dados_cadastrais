import mysql.connector
from mysql.connector import connect, cursor


#=================================================================================
# CAMPOS DE CONEXÃO COM O BANCO DE DADOS
#=================================================================================
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
    print("\nConexão estabelecida!\n")
    cursor = connection.cursor()
except mysql.connector.Error as err:
    print(err)
    
# CRIAÇÃO DA DATABASE E TABELAS
cursor.execute("CREATE DATABASE IF NOT EXISTS dados_cadastrais")
cursor.execute("USE dados_cadastrais")
cursor.execute("CREATE TABLE IF NOT EXISTS info_cadastrais(id INT AUTO_INCREMENT, Nome VARCHAR(100), Cpf VARCHAR(20), Endereço VARCHAR(100), Telefone VARCHAR(20), Email VARCHAR(100), Data_Nascimento VARCHAR(100), Idade INT(4), Sexo VARCHAR(2), primary key (id))")


#=================================================================================


#=================================================================================
# CAMPOS DE VALIDAÇÃO DE INPUT
#=================================================================================

def valida_nome(Nome):
    while True:
        if not Nome.isnumeric():
            break
        else:
            print("Por favor, use apenas letras.\n")
            Nome = str(input("Digite o nome: ")).title()
    return Nome

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
    return Cpf

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
    return Telefone

def valida_email(Email):
    while True:
        if '@' in Email and '.com' in Email:
            break
        else:
            print("Revise o email por favor, e tente novamente.\n")
            Email = str(input("Digite o e-mail: ")).lower()
    return Email

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
    return Data_Nascimento
      
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
    return Sexo
#=================================================================================


#=================================================================================
# CAMPOS DE FUNÇÕES
#=================================================================================
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

# FUNÇÃO DE CONSULTA
def consulta_base():
    cursor.execute("SELECT * FROM info_cadastrais")
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA DE ID
def consulta_id():
    id = str(input("\nDigite o ID do cadastro que deseja consultar: "))
    cursor.execute("SELECT * FROM info_cadastrais WHERE id = {}".format(id))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA DE ID E VALORES ESPECÍFICOS
def consulta_id_valores():
    id = str(input("\nDigite o ID do cadastro que deseja consultar: "))
    valores = str(input("\nDigite os valores que deseja pesquisar separados por virgula: "))
    valores = valores.split(',')
    valores = tuple(valores)
    cursor.execute("SELECT * FROM info_cadastrais WHERE id = {}".format(id))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        for valor in valores:
            if valor in registro:
                print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA PELO NOME
def consulta_nome():
    Nome = str(input("\nDigite o nome que deseja pesquisar: ")).title()
    cursor.execute("SELECT * FROM info_cadastrais WHERE Nome = '{}'".format(valida_nome(Nome)))   
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA PELO CPF
def consulta_cpf():
    Cpf = str(input("\nDigite o CPF que deseja pesquisar: "))
    valida_cpf(Cpf)
    cursor.execute("SELECT * FROM info_cadastrais WHERE Cpf = '{}'".format(valida_cpf(Cpf)))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA PELO ENDEREÇO
def consulta_endereco():
    endereco = str(input("\nDigite o endereço que deseja pesquisar: "))
    cursor.execute("SELECT * FROM info_cadastrais WHERE Endereco = '{}'".format(endereco))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA PELO TELEFONE
def consulta_telefone():
    Telefone = str(input("\nDigite o telefone que deseja pesquisar: "))
    valida_telefone(Telefone)
    cursor.execute("SELECT * FROM info_cadastrais WHERE Telefone = '{}'".format(valida_telefone(Telefone)))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA PELO E-MAIL
def consulta_email():
    Email = str(input("\nDigite o e-mail que deseja pesquisar: "))
    valida_email(Email)
    cursor.execute("SELECT * FROM info_cadastrais WHERE E-mail = '{}'".format(valida_email(Email)))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))

    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA PELA IDADE
def consulta_idade():
    idade = str(input("\nDigite a idade que deseja pesquisar: "))
    cursor.execute("SELECT * FROM info_cadastrais WHERE Idade = '{}'".format(idade))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nE-mail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE CONSULTA PELA DATA DE NASCIMENTO
def consulta_data_nascimento():
    Data_Nascimento = str(input("\nDigite a data de nascimento que deseja pesquisar: "))
    valida_nascimento(Data_Nascimento)
    cursor.execute("SELECT * FROM info_cadastrais WHERE Data_Nascimento = '{}'".format(valida_nascimento(Data_Nascimento)))
    # Recuperando todos os registros
    dados = cursor.fetchall()
    # Imprimindo os resultados
    for registro in dados:  
        print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

# FUNÇÃO DE ALTERAÇÃO PELO ID
def altera_pelo_id():
    id_alterar = str(input("\nDigite o ID que deseja alterar: "))
    Nome = str(input("\nDigite o novo nome: ")).title()
    valida_nome(Nome)
    
    CPF = str(input("Digite o novo CPF: "))
    valida_cpf(CPF)
    
    Endereco = str(input("Digite o novo endereço: ")).title()
    
    Telefone = str(input("Digite o novo telefone: "))
    valida_telefone(Telefone)
    
    Email = str(input("Digite o novo e-mail: "))
    valida_email(Email)
    
    Data_Nascimento = str(input("Digite a nova data de nascimento: "))
    valida_nascimento(Data_Nascimento)
    
    Idade = str(input("Digite a nova idade: "))
    
    Sexo = str(input("Digite o novo gênero: ")).title()
    valida_sexo(Sexo)

    # ATUALIZAÇÃO DOS DADOS CADASTRAIS
    cursor.execute("UPDATE info_cadastrais SET Nome = '{}', CPF = '{}', Endereço = '{}', Telefone = '{}', Email = '{}', Data_Nascimento = '{}', Idade = '{}', Sexo = '{}' WHERE id = '{}'".format(Nome,CPF,Endereco,Telefone,Email,Data_Nascimento,Idade,Sexo,id_alterar))
    
    # Commitar query e fechar conexões
    connection.commit()
    cursor.close()
    connection.close()

    print("Dados atualizados com sucesso!")

# FUNÇÃO DE DELETAÇÃO PELO ID
def deleta_pelo_id():
    while True:
        id_deletar = str(input("\nDigite o ID que deseja deletar: "))
        cursor.execute("SELECT * FROM info_cadastrais WHERE id = {}".format(id_deletar))
        # Recuperando todos os registros
        dados = cursor.fetchall()
        # Imprimindo os resultados
        for registro in dados:
            print("\nid: {}\nNome: {}\nCPF: {}\nEndereço: {}\nTelefone: {}\nEmail: {}\nData de Nascimento: {}\nIdade: {}\nGênero: {}\n".format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5],registro[6],registro[7],registro[8]))
        
        choice = input("Confirme se é esse o registro que gostaria de deletar? [S/N]: ").upper()
        if choice == "S":
            cursor.execute("DELETE FROM info_cadastrais WHERE id = {}".format(id_deletar))
            # Commitar query e fechar conexões
            connection.commit()
            cursor.close()
            connection.close()
            print("Registro deletado com sucesso!")
            break
        elif choice == "N":
            print("Por favor selecione o registro correto")
        else:
            print("\nOpção inválida!")
            

#=================================================================================
# MENU PRINCIPAL
#=================================================================================
while True:
    print("#=================================#")
    print("          MENU PRINCIPAL ")
    print("#=================================#")

    print("\n1 - Cadastrar\n2 - Consultar Base\n3 - Consultar pelo Id\n4 - Consultar Id Valores\n5 - Consultar Nome\n6 - Consultar CPF\n7 - Consultar Endereço\n8 - Consultar Telefone\n9 - Consultar Email\n10 - Consultar Data de Nascimento\n11 - Consultar Idade\n12 - Alterar pelo Id\n13 - Deletar pelo Id\n14 - Sair")
    
    opcao = int(input("\nDigite a opção que deseja: "))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        consulta_base()
    elif opcao == 3:
        consulta_id()
    elif opcao == 4:
        consulta_id_valores()
    elif opcao == 5:
        consulta_nome()
    elif opcao == 6:
        consulta_cpf()
    elif opcao == 7:
        consulta_endereco()
    elif opcao == 8:
        consulta_telefone()
    elif opcao == 9:
        consulta_email()
    elif opcao == 10:
        consulta_data_nascimento()
    elif opcao == 11:
        consulta_idade()
    elif opcao == 12:
        altera_pelo_id()
    elif opcao == 13:
        deleta_pelo_id()
    elif opcao == 14:
        break
    else:
        print("\nOpção inválida!")
    