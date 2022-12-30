# importa o arquivo tarefa_secundaria
#import argparse

from tarefa_secundaria import conecta_no_banco_de_dados, cria_tabela_afazers, ler_informações_sobre_afazer,insere_afazer_no_banco_de_dados
# Chama todas as funções
conexao = conecta_no_banco_de_dados("todo.db")
cria_tabela_afazers(conexao)

# Parte de logica de programação
escolha = input("Quer inserir informações na tabela afazer? digite S para sim e N para não: ")
if escolha == "S":
    afazer = ler_informações_sobre_afazer(conexao)
 #   insere_afazer_no_banco_de_dados()



'''
parser = argparse.ArgumentParser(
    description="Gerencia lista de afazeres.",
    epilog="Script para controlar a lista de afazeres",
    add_help=True,
)
parser.add_argument(
    "--create_todo",
    help="Insere um novo afazer na lista de afazeres.",
    action="Store_true", # Transforma essa opção em um argumento booleano!
)



args = parser.parse_args()

if args.create_todo:
    afazer = ler_informações_sobre_afazer()
    insere_afazer_no_banco_de_dados(conexao, afazer)

'''


    
    
