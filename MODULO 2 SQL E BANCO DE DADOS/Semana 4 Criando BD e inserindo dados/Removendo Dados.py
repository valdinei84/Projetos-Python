# criar um programa que remova pedidos com base no id da seguinte forma:
import sqlite3
conexao = sqlite3.connect("Aula_Semana4")
cursor = conexao.cursor()
pedido_id = input("Qual o ID do pedido que deseja remover? ")
valores = [pedido_id]
sql = "delete from pedido where id = ?"
cursor.execute(sql, valores)
conexao.commit()
conexao.close()