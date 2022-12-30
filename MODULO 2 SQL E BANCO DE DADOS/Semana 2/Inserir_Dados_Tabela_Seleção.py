
import sqlite3
conexao = sqlite3.connect("teste")
cursor = conexao.cursor()
sql = '''
    INSERT INTO selecao (id, nome, titulos, confederacao) VALUES 
        (2, "Argentina", 2, "conmebol"),
        (3, "Alemanha", 4, "uefa"),
        (4, "Italia", 4, "uefa"),
        (5, "França", 2, "uefa"),
        (6, "México", 0, "concacaf"),
        (7, "Japão", 0, "afc"),
        (8, "Senegal", 0, "afc");
        
'''
cursor.execute(sql)
conexao.commit()
conexao.close()