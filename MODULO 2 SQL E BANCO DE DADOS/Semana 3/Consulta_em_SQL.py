import sqlite3
conexao = sqlite3.connect("teste")
cursor = conexao.cursor()
sql = '''
    select id, nome, titulos, confederacao from selecao where titulos >= 4
'''
resultados = cursor.execute(sql)
for resultado  in resultados:
    print(resultado)
print("Fim do programa")
conexao.close()