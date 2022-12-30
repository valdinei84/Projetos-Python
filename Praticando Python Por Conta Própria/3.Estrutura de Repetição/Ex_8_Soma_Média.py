# Exercício 8
# Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = input("Digite uma liste de valores separados por espaços: ")
print(f"Os valores digitados foram: {lista}")
lista = lista.split()
for i in range(len(lista)):
    lista[i] = int(lista[i])


print("soma: ", sum(lista))
print("média: ", sum(lista)/len(lista))