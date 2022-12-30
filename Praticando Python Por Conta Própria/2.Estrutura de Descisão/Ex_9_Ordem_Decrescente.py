# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input("Informe o Primeiro Número: "))
n2 = int(input("Informe o Segundo Número: "))
n3 = int(input("Informe o Terceiro Número: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        # OK
        print(f"1º {n1}, 2º {n2}, 3º {n3}")
    else: 
        # OK
        print(f"1º {n1}, 2º {n3}, 3º {n2}")
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        # OK
        print(f"1º {n2}, 2º {n1}, 3º {n3}")
    else: 
        # OK
        print(f"1º {n2}, 2º {n3}, 3º {n1}")

else: 
    if n1 > n2:
        # OK
        print(f"1º {n3}, 2º {n1}, 3º {n2}")
    else: 
        # OK
        print(f"1º {n3}, 2º {n2}, 3º {n1}")