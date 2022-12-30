import sqlite3
conexao = sqlite3.connect("Aula_Semana4")
'''
sql_cliente = 
CREATE TABLE cliente (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NOME TEXT (100),
    cpf TEXT (14) NOT NULL,
    CONSTRAINT cliente_UN UNIQUE (cpf)
);
'''
'''
sql_pedido = 
CREATE TABLE pedido (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "data" TEXT(20) NOT NULL,
    cliente_id INTEGER NOT NULL,
    CONSTRAINT pedido_FK FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);
'''
sql_item_pedido = '''
CREATE TABLE item_pedido (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto TEXT(100),
    valor REAL,
    quantidade INTEGER,
    CONSTRAINT intem_pedido_FK FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);
'''
cursor = conexao.cursor()
cursor.execute(sql_item_pedido)
conexao.commit()
conexao.close()