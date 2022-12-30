import sqlite3 # importação da linguagem do banco de dados no caso
conexao = sqlite3.connect("banco_pd922") # Conexão com o dbeaver
cursor = conexao.cursor() # Associar a conexão
# padra para fazer sempre so muda o nome banco_pd922 para o nome que voce quiser
sql = '''
    CREATE TABLE produto (
        id int not null,
        nome VARCHAR(50),
        categoria_id int not null,
        primary key (id),
        foreign key (categoria_id) references categoria (id))
    );
'''
cursor.execute(sql)
conexao.commit()
conexao.close()
