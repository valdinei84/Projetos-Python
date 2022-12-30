# Exercício 1
# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.

notas = []
while True:
    print("Digite -1 para encerrar o programa")
    nota = float(input("Digite uma nota de 0 a 10: "))
    if nota > 10:
        print("Valor Inválido")
    if nota == -1:
        break
