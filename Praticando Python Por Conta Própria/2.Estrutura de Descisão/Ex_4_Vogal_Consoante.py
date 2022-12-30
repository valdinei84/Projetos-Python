# Faça um Programa que verifique se uma letra digitada é vogal ou consoante
letra = str(input("Digite uma letra qualquer "))
vogais = 'aeiou'
if letra in vogais or letra in vogais.upper():
    # função (.upper) converte letras minusculas e maiúsculas
    print("Vogal")
else:
    print("Consoante")