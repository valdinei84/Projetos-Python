# Exercício 7
# Faça um programa que leia 5 números e informe o maior número.

lista = input("Digite uma lista de valores separadoos por espaços: ")
lista = lista.split() # SPLIT ele iguala os espaços entre os numeros 
for i in range(len(lista)): # o LEN ele pega o tamanho da lista 
    lista[i] = int(lista[i]) # converte para numeros inteiros
print("O maior numero é", max(lista)) # o MAX ele puxa o maior valor da lista


    
    
    
    