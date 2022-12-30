id = input("Digite o ID do Fornecedor: ")
nome = input("Digite o Nome do Fornecedor: ")
endereco = input("Digite o Endereco do Fornecedor: ")

import sqlite3
conexao = sqlite3.connect("teste")
cursor = conexao.cursor()
sql = '''
    INSERT INTO teste (id, nome, endereco) VALUES (?, ?, ?)
'''
valores = [id, nome, endereco]
cursor.execute(sql, valores)
conexao.commit()
print("DADOS INSERIDOS COM SUCESSO!")
conexao.close()