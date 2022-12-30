import sqlite3
conexao = sqlite3.connect("teste")
cursor = conexao.cursor()
sql = '''
    CREATE TABLE selecao (
        id INTEGER NOT NULL,
        nome TEXT (100),
        titulos INTEGER,
        confederacao TEXT (10),
        CONSTRAINT selecao_PK PRIMARY KEY (id)
    );
'''
cursor.execute(sql)
conexao.commit()
conexao.close()