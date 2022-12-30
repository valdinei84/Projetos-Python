
# Exercício 11
# Altere o programa anterior para mostrar no final a soma dos números.

x = int(input("Digite um numero "))
y = int(input("Digite um numero !!Esse número deve ser maior que o primeiro "))
soma = 0
for i in range(x, y+1):
    soma = soma + i
    print(i, end =" - ")
    print(soma)
    
    
# em aberto não finalizado