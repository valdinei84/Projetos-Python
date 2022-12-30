import sqlite3
conexao = sqlite3.connect("aula_semana3")
cursor = conexao.cursor()
# Criando Tabela
'''
sql = 
    CREATE TABLE fornecedor(
        id INT, nome VARCHAR (100), 
        endereco VARCHAR (100)
        );
'''
# Inserindo informções
'''
sql = 
   INSERT INTO fornecedor (id, nome, endereco) VALUES 
   (3, "Ubr", "Rio de Janeiro"),
   (2, "ultima", "Curitiba");
'''
# Deixando o próprio usuário colocar as informações
'''
id = input("Digite o seu id: ")
nome = input("Digite o seu nome: ")
endereço = input("Digite o seu endereço: ")

sql_inserir = 'INSERT INTO fornecedor (id, nome, endereco) VALUES (?, ?, ?)'
valores = [id, nome, endereço] # Lista com os valores que o usuário digitou
print("Usuário cadastrado com sucesso")

cursor.execute(sql_inserir, valores) # vai substituir automáticamnte os potos de interrogação pelos valores que o usuário digitou

'''
# selecionar dados
#sql_select = "SELECT * FROM fornecedor"
sql_select = 'SELECT nome FROM fornecedor WHERE nome = "Valdinei"' 
resultados = cursor.execute(sql_select)

for fornecedor in resultados:
    print(fornecedor)
    
conexao.commit() # comando responsável por enviar as informações para o dbeaver
conexao.close() # comando para encerrar a conexão