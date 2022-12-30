# fassa um programa que possa atualizar os dados de um determinado cliente, 
# fornecendo o id dele.
import sqlite3
conexao = sqlite3.connect("Aula_Semana4")
cursor = conexao.cursor()
cliente_id = input("Qual o ID do cliente que deseja atualizar? ")
nome = input("Informe o novo nome do cliente: ")
cpf = input("Informe o novo CPF do cliente: ")
sql = '''
update cliente set nome = ?, cpf = ? where id = ?
'''
valores = [nome, cpf, cliente_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()