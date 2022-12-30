'''
Crie um programa em Python que gere tabelas para uma aplicação de eventos. 
Elas devem compreender as seguintes funcionalidades:
a - Eventos devem ter título, data e local, além da referência ao organizador;
b - O organizador deve ter nome, email e cpf;
c - As restrições/relacionamentos devem fazer sentido.
'''
import sqlite3
conexao = sqlite3.connect("Gerador_Tabela")
print("Sisema de Eventos")
sql = '''
create table eventos (
    titulo text(30),
    data text(10),
    endereco text (100)
);
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()

# nao concluido