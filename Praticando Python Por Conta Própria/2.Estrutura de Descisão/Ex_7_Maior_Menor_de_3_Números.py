# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
print(f"Os números digitados foram: {n1}, {n2}, {n3}")

# Primeira parte
if n1 > n2 and n2 > n3:
    print(f"O maior numero é: {n1}, e o menor é {n3}")
# Segunda parte
elif n2 > n1 and n2 > n3:
    print(f"O maior número é: {n2}, e o menor é {n3}")
# Terceira parte
elif n3 > n2 and n2 > n1:
    print(f"O maior número é: {n3}, e o menór é: {n1}")
# Quarta parte
elif n3 > n2 and n2 > n3:
    print(f"O maior número é: {n2}, e o menor é: {n1}")
# Quinta parte
elif n1 > n3 and n3 > n2:
    print(f"O maior número é: {n1}, e o menor é: {n2}")