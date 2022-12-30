# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

Sexo = str(input("Digite seu sexo, M para Masculino e F para Femenino: "))
if Sexo == "M":
    print("Masculino")
elif Sexo == "F":
    print("Femenino")
if Sexo != "M" and Sexo != "F":
    print("Sexo inválido, vá para o médico!!")
