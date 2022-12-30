# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Qual seu horário de trabalho: M para Matution, V para Vespertino ou N para Noturno ")
letra = (str(input()))

if letra == "m":
    print("Bom Dia")
elif letra == "v":
    print("Boa Tarde")
elif letra == "n":
    print("Boa Noite")
    