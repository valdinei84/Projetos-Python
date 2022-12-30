'''Módulo de funçães do banco de dados.'''

import sqlite3
import datetime

def conecta_no_banco_de_dados(nome_db: str):
    '''Conecta no banco de dados.'''
    conexao = sqlite3.connect(nome_db)
    return conexao


def cria_tabela_de_afazeres(conexao):
    '''Cria a tabela de afazeres, se ela não existir.'''
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tb_afazeres (
            id int not null autoincrement,
            descricao text(100),
            status text(30),
            categoria text(30),
            data_criacao text(10),
            data_finalizacao text(10),
            data_prevista_finalizacao text(10),
            recorrencia text(30)
        );
        '''
    )
    
    
    
def ler_informações_sobre_afazer():
    '''Solicita as informações de um afazer para o usuário.
    '''
    print("Por favor preencha as informçãoes relacionadas à tarefa.")
    descricao = input("Digite uma descrição para a tarefa: ")
    status = input("Digite um status para a tarefa: ")
    categoria = input("Em qual categoria essa tarefa se encaixa? ")
    data_criacao = datetime.now()
    data_finalizacao = ""
    data_prevista_finalizacao = input("Qual a data prevista para finalização? ")
    recorrencia = input("Essa tarefa possui alguma recorrência? ")
    
    return (
        descricao, 
        status, 
        categoria, 
        data_criacao, 
        data_finalizacao, 
        data_prevista_finalizacao, 
        recorrencia
    )
    
    
def insere_afazer_no_banco_de_dados(conexao, afazer: tuple[str]):
    cursor = conexao.cursor()
    
    cursor.execute("""
    INSERT INTO tb_afazeres (
        descricao,
        status,
        categoria,
        data_criacao,
        data_prevista_Finalizacao,
        recorrencia
    ) 
        VALUES(?, ?, ?, ?, ?, ?, ?")""",
    afazer,
    )
    
    conexao.commit()
    print("Registro inserido com sucesso!")
    

'''Criação da tabela categoria'''    
def criar_tabela_categoria(conexao, categoria):
    cursor = conexao.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tb_categoria(
                       id int not null autoincrement,
                       nome text (30),
                       categoria text(30),
                       funcao text (15),
                       data_de_validade text (10)
                       );
                   """
    )
def ler_informações_sobre_categoria():
    '''Solicita as informações de uma categoria para o usuário.
    '''
    print("Por favor preencha as informçãoes relacionadas à categoria.")
    nome = input("Digite um nome para categoria: ")
    categoria = input("Digite um status para a tarefa: ")
    funcao = input("Qual função para essa categoria ")
    data_de_entrada = datetime.now()
    data_de_validade = data_de_entrada
    
    
    return (
        nome, 
        categoria, 
        funcao, 
        data_de_entrada, 
        data_de_validade, 
    )
def insere_categoria_no_bando_de_dados(conexao, categoria):
    '''
    INSERT INTO categoria categoria 
    (
        nome,
        categoria, 
        funcao,
        data_de_entrada,
        data_d_validade
        )
        VALUES(?, ?, ?, ?, ?)
    ''', conexao, categoria