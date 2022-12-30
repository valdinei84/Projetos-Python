import sqlite3
import datetime
conexao = sqlite3.connect("Aula_Semana4")
print("Insira os dados do Pedido")
cliente_id = input("Qual o ID do Cliente? ")
hoje = datetime.date.today() # A variavel Hoje vai receber automaticamente a data atualizada
valores = [cliente_id, hoje]
sql_pedido = 'INSERT INTO pedido (cliente_id, data) VALUES (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_pedido, valores) # para executar a função
print("ID do pedido:", cursor.lastrowid) # indica qual foi o último ID gerado automaticamente
