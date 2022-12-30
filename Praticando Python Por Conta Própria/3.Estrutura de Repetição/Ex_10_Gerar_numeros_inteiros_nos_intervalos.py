# Exercício 10
# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
numero1 = int(input("Informe um número inteiro "))
numero2 = int(input("informe um número inteiro "))

for i in range(numero1, numero2+1):
    print(i, end=' ')