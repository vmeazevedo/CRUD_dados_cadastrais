###########################################################################
# Conexão com o banco de dados	
host = "localhost"
user = "root"
password = ""

connection = mysql.connector.connect(
    host=host,
    user=user, 
    password=password)
###########################################################################
# Criação da database e tabela
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS dados_cadastrais")
cursor.execute("USE dados_cadastrais")
cursor.execute("CREATE TABLE IF NOT EXISTS info_cadastrais(id INT AUTO_INCREMENT, Nome VARCHAR(100), CPF VARCHAR(20), Endereço VARCHAR(100), Telefone VARCHAR(20), E-mail VARCHAR(100), Data_Nascimento VARCHAR(100), Idade VARCHAR(4), Sexo VARCHAR(2))")
###########################################################################