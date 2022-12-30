# Crie de forma recursiva uma função que printe do número recebido até o zero.
def contagem_decrescente(numero):
    print(numero)
    if numero > 0:
        contagem_decrescente(numero-1)
numero = int(input())
contagem_decrescente(numero)