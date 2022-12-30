# Construir m jogo em que o usuário tenta adivinhar um número aleatório.
# O computador (programa) vai escolher um número aleatório
# Esse número aleatório é entre 1 e 50
# Quando o usuário acertar, imprimir uma mensagem que ele ganhou.
# Quando o usuário perder imprimir uma mensagem que ele perdeu o jogo
# Número de tentativas: 5

    
from random import random
import statistics

# 1 - O programa deve sortear um número
numero_secreto = random.randint(1, 50)
print (numero_secreto)

# 1.1 - Definir numero de tentativas
tentativa = 1

# 2 - Solicitar um número para o usuário
palpite = int(input("Qual é seu palpite de 1 a 50? "))

while tentativa <= 5:
# 3 - Comparar a entrada do usuário com o número secreto
    if numero_secreto != palpite:
        tentativa = tentativa + 1
        print("Você errou!")
        palpite = int(input("Digite outro palpite! "))
    else:
        print(f"Você venceu com {tentativa} tentativas!")
        break

if tentativa > 5:
    print("Você perdeu!")