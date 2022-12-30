import sqlite3
conexao = sqlite3.connect("teste")
cursor = conexao.cursor()
sql = '''
    CREATE TABLE restaurante (
        id not null primary key autoincrement, 
        nome text (100) not null, 
        estrelas int,
        zona text (20)
        );
'''
cursor.execute(sql)
conexao.commit()
conexao.close()