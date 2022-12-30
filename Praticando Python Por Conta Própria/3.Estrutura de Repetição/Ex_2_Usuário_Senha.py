# Exercício 2
# Faça um programa que leia um nome de usuário e a sua senha, 
# e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    usuario = input("Digite o nome para usuário ")
    password = input("Informe uma senha ")
    
    if password != usuario:
        print("Acesso Liberado")
        break
    else:
        print("Acesso Negado")