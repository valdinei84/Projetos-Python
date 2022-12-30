import sqlite3 # importa a pasta para dentro do python
conexao = sqlite3.connect("db.sqlite3") 
cursor = conexao.cursor() # cursor para executar comandos SQL, tanto os DML como os DDL
cursor.execute("CREATE TABLE Fornecedor (id INT, name VARCHAR(100), endereco VARCHAR(250));")
conexao.commit() # A função “commit”, associada à variável “conexao”, chamada logo em seguida, 
                # serve para efetivamente salvar as alterações realizadas no banco de dados. 
conexao.close() # é chamada para fechar a conexão
