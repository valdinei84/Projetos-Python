'''
Exercício 5
Altere o programa anterior permitindo ao usuário informar as populações e as taxas 
de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
ano = 0
popA = int(input("Qual a População da sua Cidade? "))
popB = int(input("Qual a População da sua Cidade? "))
taxaA = float(input("Informe a taxa de crescimento A: "))
taxaB = float(input("Informe a taxa de crescimento B: "))
6
while True:
    ano += 1
    print("ano", ano)
    popA = popA + taxaA/100*popA
    popB = popB + taxaB/100*popB
    print(f"População A: {popA:.2f} População B: {popB:.2f}")
    if popA >= popB:
        print(f"Após {ano} anos")
        print(f"A população da cidade A foi de {popA:.2f}, e a cidade B foi de {popB:.2f}")
        print(f"A Taxa da cidade A foi de {taxaA:.2f}, e da cidade B foi de {taxaB:.2f}")

        break