# vamos permitir que o usuário indique quais e quantos itens ele deseja associar ao pedido.
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
pedido_id = cursor.lastrowid
quantidade_itens = input("Quantos itens deseja adicionar? ")
quantidade_itens = int (quantidade_itens)
for i in range(quantidade_itens+1):
    produto = input("Qual o produto? ")
    quantidade = input("Qual a quantidade? ")
 #   quantidade = int(quantidade)
    valor = input("Qual o valor? ")
    valor = float(valor)
    sql_item = '''
    INSERT INTO item_pedido
    (pedido_id, produto, valor, quantidade)
    VALUES
    (?, ?, ?, ?)
    '''
    valores = [pedido_id, produto, valor, quantidade]
    cursor.execute(sql_item, valores)
    
conexao.commit()
conexao.close()