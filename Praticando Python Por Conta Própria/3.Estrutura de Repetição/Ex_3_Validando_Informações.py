# Exercício 3
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Digite seu nome: "))
while len(nome) <= 3:
    nome = str(input("Nome inválido. Digite seu nome novamente: "))
    
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = str(input("Idade inválida. Digite outra idade: "))
    
salário = float(input("Digite seu salário: "))
while salário < 0:
    salário = float(input("Salário incorreto. Digite novamente seu salário: "))

Sexo = str(input("Digite se voce é (m) para masculino ou (f) para femenino "))
while Sexo != 'f' and Sexo != 'm':
    Sexo = str(input("Sexo inválido. Digite novamente o bagulho: "))
    
Estado_Civil = str(input("Digite seu estado civil: 's', 'c', 'v', 'd' "))
while Estado_Civil != 's' and Estado_Civil != 'c' and Estado_Civil != 'v' and Estado_Civil != 'd':
    Estado_Civil = str(input("Estado Civil incorreto. Por favor digite novamente: "))