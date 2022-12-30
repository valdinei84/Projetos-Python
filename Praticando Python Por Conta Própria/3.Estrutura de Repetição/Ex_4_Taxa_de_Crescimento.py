'''
Exercício 4
Supondo que a população de um país A seja da 
ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.'''
ano = 0
popA = 80000
popB = 200000

while True:
    ano += 1
    print("ano", ano)
    popA = popA + 0.03*popA
    popB = popB + 0.014*popB
    print("popA:", popA, "popB:", popB)
    if popA >= popB:
        print(f"Após {ano} anos")
        break
    