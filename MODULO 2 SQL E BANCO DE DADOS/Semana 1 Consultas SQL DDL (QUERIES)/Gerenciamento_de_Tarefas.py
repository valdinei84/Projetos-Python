'''
Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. 
As tabelas devem compreender as seguintes funcionalidades:
a - As tarefas devem ser divididas em “categorias”;
b - Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
c - As restrições/relacionamentos devem fazer sentido.
'''
'''
import sqlite3 # importa a pasta SQL  para dentro do python
 # deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
tabela = input("Digite o nome para tabela ")
nome = input("Digite seu nome completo: ")
Endereço = input("Digite seu endereço: ")
data = input("Digite a data de hoje: ")
tarefa = input("Essa tarefa esta concluida? ")

conexao = sqlite3.connect("db.sqlite3") # Conecta o banco de dados com Python
cursor = conexao.cursor() # cursor para executar comandos SQL, tanto os DML como os DDL
cursor.execute(f"Create table {tabela} (id, {nome}, varchar(100), {Endereço} varchar(250), {data} date, status de conclusão {tarefa} varchar (3);")
conexao.commit() # A função “commit”, associada à variável “conexao”, chamada logo em seguida, 
                 # serve para efetivamente salvar as alterações realizadas no banco de dados. 
conexao.close()  # é chamada para fechar a conexão
'''
import sqlite3 # importa a pasta para dentro do python
nome_da_tabela = input("Digite o nome da Tabela: ")

conexao = sqlite3.connect("db.sqlite3") 
cursor = conexao.cursor() # cursor para executar comandos SQL, tanto os DML como os DDL
cursor.execute(f"CREATE TABLE {nome_da_tabela} (id INT, name VARCHAR(100), endereco VARCHAR(250));")

for i in range(10):
    ID = str(i)
    nome = 'nome-' + str(i)
    enderco = "Endereco" + (i)
    
    cursor.execute(f"insert into {nome_da_tabela} values({ID}, '{nome}', '{enderco}'); ")
    
    
conexao.commit() # A função “commit”, associada à variável “conexao”, chamada logo em seguida, 
                # serve para efetivamente salvar as alterações realizadas no banco de dados. 
conexao.close() # é chamada para fechar a conexão

# teste de alteração
