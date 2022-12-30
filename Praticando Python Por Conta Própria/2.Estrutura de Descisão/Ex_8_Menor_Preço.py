# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
x = float(input("Priemiro Valor: "))
y = float(input("Segundo Valor: "))
z = float(input("Terceiro Valor: ")) 
# Quando tens que diferenciar mais do que um valor usa-se o elif
if x < y and x < z:
    print(f"O mais barato é o que custa {x} R$")
elif y < x and y < z:
    print(f"O mais barato é o que custa {y} R$")
elif z < y and z < x:
    print(f"O mais barato é o que custa {z} R$")