# Exercício 14
# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e a quantidade de números impares.

num = [[], []]
valor = 0
for c in range (1, 11): # aqui ele vai dizer que vai receber 10 numeros inteiros
    valor = int(input(f"Digite o {c}º. valor: "))
    if valor % 2 == 0:
        num [0].append(valor)
    else:
        num[1].append(valor)
print("-=" * 30)
num[0].sort()
num[1].sort()
print(f"Os Valor(es pares digitados foram: {num[0]}")
print(f"Os Valores pares impares foram: {num[1]}")