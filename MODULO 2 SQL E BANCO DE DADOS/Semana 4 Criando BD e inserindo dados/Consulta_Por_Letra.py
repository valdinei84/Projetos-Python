# 2 — Quantos clientes tem a letra "M" no início do nome?
import sqlite3
conexao = sqlite3.connect("Aula_Semana4")
cursor = conexao.cursor()
sql = '''
select * from cliente where nome like 'M%'
'''
consulta = cursor.execute(sql)
for resultado in consulta:
    print(resultado)