
from datetime import date
import sqlite3
conexao = sqlite3.connect("todo.db")
cursor = conexao.cursor()
'''
    SUMÁRIO
    Menu e Criação de Tabelas
# 1.0 - menu de escolha linha 13 (pg.33)
# 1.1 - Cria a tabela Afazer (pg.53)
# 1.2 - Cria a tabela Categoria (pg.73)
    Inserção de Itens
# 2.0 - pedindo informações para inserir na tabela afazer (pg.89)
# 2.1 - chama a tabela  no indice 1.6 para inserir as informações no banco de dados (pg.100)
# 2.2 - Insere os informações dentro do banco de dados (pg.111)
# 2.3 - Pede as informações para inserir na tabela Categoria (pg.134) 
# 2.4 - chama a tabela  no indice 1.8 para inserir as informações no banco de dados (pg.141) 
# 2.5 - Insere os informações dentro do banco de dados (pg.148)
    Atualizando Tabelas
# 3.0 - Atualiza as tabelas que escolher atualizar (pg.167)
    Seleção de Tabelas
# 4.0 - Comando para seleção de opções tabelas (pg.187)
    Deletando tabelas
# 5.0 - Deletar ID (pg.203)
    Listando Tabelas
# 6.0 - Listar todos os afazeres de um dia específico (pg.221)
# 6.1 - Listar todas as categorias (pg.237)
'''




# 1.0 - menu de escolha
def menu ():
    cria_tabela_afazers()
    cria_tabela_categoria()
    opcao = input("Qual opção? 1-Inserir na Tabela Afazeres, 2-Inserir na Tabela Categoria, 3-Alterar, 4-Deletar Tabelas, 5-Deletar ID, 6-Filtrar Iformações, 7-Filtrar Categoria: ")
    if opcao == "1":
        ler_informações_sobre_afazer()
    elif opcao == "2":
        ler_informações_sobre_categoria()
    elif opcao == "3":
        atualizar_tabela_afazer()
    elif opcao == "4":
        deletar_tabelas()
    elif opcao == "5":
        deletar_id()
    elif opcao == "6":
        lista_afazeres_por_data_criacao()
    elif opcao == "7":
        lista_todas_categorias()

# 1.1 - Cria a tabela Afazer
def cria_tabela_afazers ():
    cursor = conexao.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS tb_afazeres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT (100),
            status TEXT (30),
            categoria TEXT (30),
            data_criacao TEXT(10),
            data_finalizacao TEXT(10),
            data_prevista_finalizacao TEXT(10),
            recorrencia TEXT (30)
        );
    '''
    cursor.execute(sql)
    conexao.commit()
#    print("Banco de Dados Afazeres Criado Com Sucesso!")
    

# 1.2 - Cria a tabela Categoria    
def cria_tabela_categoria():
    cursor = conexao.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS tb_categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao varchar (50),
            data_criacao varchar (15),
            data_vencimento 
        );
    '''
    cursor.execute(sql)
    conexao.commit()
#    print("Banco de Dados Categoria Criado Com Sucesso!")
    
    
# 2.0 - pedindo informações para inserir na tabela afazer 
def ler_informações_sobre_afazer():
    print("Por favor preencha as informçãoes relacionadas à tarefa.")
    descricao = input("Digite uma descrição para a tarefa: ")
    status = input("Digite um status para a tarefa: ")
    categoria = input("Em qual categoria essa tarefa se encaixa? ")
    data_criacao = date.today()
    data_finalizacao = input("Digite a data para finalização: ")
    data_prevista_finalizacao = input("Qual a data prevista para finalização? ")
    recorrencia = input("Essa tarefa possui alguma recorrência? ")

# 2.1 - chama a tabela  no indice 1.6 para inserir as informações no banco de dados  
    insere_afazer_no_banco_de_dados(
        descricao, 
        status, 
        categoria, 
        data_criacao, 
        data_finalizacao, 
        data_prevista_finalizacao, 
        recorrencia
        )  
    
# 2.2 - Insere os informações dentro do banco de dados
def insere_afazer_no_banco_de_dados( descricao, status, categoria, data_criacao, data_finalizacao, data_prevista_finalizacao, recorrencia):
    dados = [descricao, status, categoria, data_criacao, data_finalizacao, data_prevista_finalizacao, recorrencia]
    sql = """
    INSERT INTO tb_afazeres (
        descricao,
        status,
        categoria,
        data_criacao,
        data_finalizacao,
        data_prevista_finalizacao,
        recorrencia
    )
        VALUES(?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, dados)
    conexao.commit()
    print("Registro inserido com sucesso!")
    opcao = input("Deseja inserir mais algum dado? Sim-1, Não-2")
    if opcao == "1":
        ler_informações_sobre_afazer()
    else:
        print("Programa finalizado")
        
# 2.3 - Pede as informações para inserir na tabela Categoria       
def ler_informações_sobre_categoria():
    print("Por favor preencha as informçãoes relacionadas à tarefa.")
    descricao = input("Digite uma descrição para a tarefa: ")
    data_criacao = input("Digite a data que foi criado: ")
    data_vencimento = input("Digite a data de vencimento: ")

# 2.4 - chama a tabela  no indice 1.8 para inserir as informações no banco de dados  
    insere_categoria_no_banco_de_dados(
        descricao, 
        data_criacao, 
        data_vencimento, 
        )  
    
# 2.5 - Insere os informações dentro do banco de dados
def insere_categoria_no_banco_de_dados(descricao, data_criacao, data_vencimento):
    dados = [descricao, data_criacao, data_vencimento]
    sql = """
    INSERT INTO tb_categoria (
        descricao,
        data_criacao,
        data_vencimento
    )
        VALUES(?, ?, ?)"""
    cursor.execute(sql, dados)
    conexao.commit()
    print("Registro inserido com sucesso!")
    opcao = input("Deseja inserir mais algum dado? Sim('1'), Não('2)")
    if opcao == "1":
        ler_informações_sobre_categoria()
    else:
        print("Programa finalizado")
        
# 3.0 - Atualiza as tabelas que escolher atualizar  
def atualizar_tabela_afazer ():
    tabela = input("Qual tabela que quer alterar: 1-Afazer, 2-Categoria ")
    coluna_a_modificar = input("Qual coluna deseja modificar?: ")
    registro = input("Digite o nome que deseja inserir: ")
    id = input("Qual ID que deseja alterar!! ")
    if tabela == "1":
        sql = (f"UPDATE tb_afazeres set {coluna_a_modificar} = '{registro}' WHERE id = {id}")
    elif tabela == "2":
        sql = (f"UPDATE tb_categoria set {coluna_a_modificar} = '{registro}' WHERE id = {id}")
    cursor.execute(sql)
    conexao.commit()
    print("Dados alterados com sucesso!")
    inicio = input("Deseja voltar ao menu inicial? Sim, Não: ")
    if inicio == "Sim":
        menu ()
    else:
        print("Programa Encerrado!!")
        

# 4.0 - Comando para seleção de opções tabelas 
def deletar_tabelas ():
    print("!!!-- ATENÇÃO UMA VEZ APAGADO PERDE TODO CONTEÚDO DA TABELA --!!!")
    prosseguir = input("Deseja prosseguir? 1-sim, 2-não: ")
    if prosseguir == "1":
        tabela = input("Digite o nome da tabel a qual deseja apagar: ")
        sql_deleta_tabela = (f"DROP TABLE {tabela}")
        print(f"{tabela} Apagada com Sucesso")
        cursor.execute(sql_deleta_tabela)
        conexao.commit()
        inicio = input("Deseja voltar ao menu inicial? Sim, Não: ")
        if inicio == "Sim":
            menu ()
        else:
            print("Programa Encerrado!!")

# 5.0 - Deletar ID
def deletar_id ():
    print("Deletar IDs")
    tabela = input("Digite o nome da tabel a qual deseja selecionar: ")
    id = input("Qual ID você quer deletar?: ")
    sql = (f"DELETE FROM {tabela} WHERE id = {id}")
    cursor.execute(sql)
    conexao.commit()
    print("ID deletado com sucesso!")
    
    inicio = input("Deseja voltar ao menu inicial? Sim-1, Não-2: ")
    if inicio == "1":
        menu ()
    else:
        print("Programa Encerrado!!")



# 6.0 - Listar todos os afazeres de um dia específico
def lista_afazeres_por_data_criacao ():
    dia = input("Qual a data que quer Buscar? ")
    sql = (f"SELECT * FROM tb_afazeres WHERE data_criacao = '{dia}'")
    cursor.execute(sql)
    for resultado in cursor:
        print(resultado)
    conexao.commit()
    
    inicio = input("Deseja voltar ao menu inicial? Sim-1, Não-2: ")
    if inicio == "1":
        menu ()
    else:
        print("Programa Encerrado!!")
        

# 6.1 - Listar todas as categorias
def lista_todas_categorias():
    tabela = input("De qual tabela sera a categoria a ser listada? ")
    sql = (f"SELECT categoria FROM {tabela}")
    cursor.execute(sql)
    for resultado in cursor:
        print(resultado)
    conexao.commit()
    
    inicio = input("Deseja voltar ao menu inicial? Sim-1, Não-2: ")
    if inicio == "1":
        menu ()
    else:
        print("Programa Encerrado!!")
menu()