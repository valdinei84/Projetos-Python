# Exercídcio 5 
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

num = [[], []]
valor = 0
valor = input("Digite uma lista de numeros aleatorios os separando por espaços: ")
valor = valor.split() # Iguala os espaços entre os números digitados
for i in (valor): # Vê o comprimeto da lista ou seja quantos elementos tem dentro da lista
    valor[i] = int(valor[i]) # transforma a lista em numeros inteiros
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print("-=" * 30)
print(f"Os números da lista foram: {num}")
print(f"Todos os valores: {num.sort[0]}")
print(f"Mostrar os valores impares{num.sort[1]}") # o .sort ele organiza os numeros em ordem crescente

# Não concluido ainda
