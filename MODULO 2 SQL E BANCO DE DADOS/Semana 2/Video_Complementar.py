import sqlite3
conexao = sqlite3.connect("db.sqlite3") # faz a conexão em parenteses é o caminho, 
# como o meu sql esta na mesma pasta basta escrever o que esta escrito la.
cursor = conexao.cursor() # responsavel por executar o comando SQL

SQL = '''
create table item_pedido (
    id int not null,
    pedido_id int not null,
    produto_id int not null,
    quantidade int not null,
    preco real not null,
    primary key (id),
    foreign key (pedido_id) references pedido(id),
    foreign key (produto_id) references produto(id)
)
'''
cursor.execute(SQL) # Aqui ele vai executar a criação da tabela, ou seja o cursor.execute vai executar a variavel SQL

conexao.commit() #  Neste momento ele vai lança os dados no banco de dados fizico que é o SQLITE3
conexao.close() # Esse comando é para finalizar a conexão