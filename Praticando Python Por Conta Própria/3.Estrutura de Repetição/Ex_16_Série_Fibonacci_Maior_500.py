# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

print("Série fibonacci")
numero = int(input("Digite um valor: Atenção esse programa so gera a série até que o valor seja maior que 500 ")) 
t1 = 0
t2 = 1
print("{} - {}".format(t1, t2), end=" ")
cont = 3
while cont < numero:
    t3 = t1 + t2
    print(" - {}".format(t3), end=" ")
    t1 = t2
    t2 = t3
    cont += 1
    print("Finished")

# nao esta pronto
    