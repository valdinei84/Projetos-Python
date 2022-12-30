import sqlite3
conexao = sqlite3.connect("Aula_Semana4")

print("Insira os dados do cliente: ")
nome = input("Qual o nome do cliente? ")
cpf = input("Qual o CPF do cliente? ")
valores = [nome, cpf]
sql_inserir = 'INSERT INTO cliente (nome, cpf) VALUES (?, ?)'
print("Seu cadastro foi efetuado com sucesso")

cursor = conexao.cursor()
cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()