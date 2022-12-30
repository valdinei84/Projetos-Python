# Faça um programa com uma função que necessite de um argumento. 
# A função deve retornar o valor de caractere ‘P’, 
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def argumentos(numero):
    if numero > 0:
        print("P")
    else:
        print("N")
numero = int(input("Digite um número "))
print(argumentos(numero))
