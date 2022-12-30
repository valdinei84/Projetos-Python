# 1 — Quais as datas dos pedidos da cliente com nome Maria da Silva?
import sqlite3
conexao = sqlite3.connect("Aula_Semana4")
cursor = conexao.cursor()
sql = '''
    select p.data from pedido as p, cliente as c where 
    p.cliente_id = c.id and c.nome = "Maria da silva"
'''
consulta = cursor.execute(sql)
for resultado in consulta:
    print(resultado)
    