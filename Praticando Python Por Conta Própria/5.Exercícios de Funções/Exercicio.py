# Criar uma função dando boas vindas a um usuario com o nome da função recebeu por parametro
def sair ():
    print("PAssei aqui tambem")
    
def multi ():
    res = input("Digite um numero ")
    resposta = res * 2
    print(resposta)
    
def boas_bindas (nome):
    print(nome)
    
def mostrar_mensagem():
    print("Entrei aqui")
nome = input("Digite um nome: ")
sair()
boas_bindas(nome) # chamando a função boas vindas
mostrar_mensagem()
multi()
