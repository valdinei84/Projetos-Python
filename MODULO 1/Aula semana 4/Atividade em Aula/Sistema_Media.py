'''
Exemplo 1
nota1 = 8.5
nota2 = 10

media = (nota1 + nota2) / 2
print(media)

# Exemplo 2
nota1 = 8.5
nota2 = 10

media = (nota1 + nota2) / 2
print(media)

if media >= 7:
    print("Aprovado")
elif (media >= 5) and (media < 7):
    print("Recuperação")
else:
    print("Reprovado")
'''
# Exemplo 3 (mais complexo)
# lendo a entrada de dados
notas = []
while True:
    nota = float(input("Digite uma nota: "))
    
    if notas == -1:
        break
    notas.append(nota)

# Calculando a media 
n_notas= len(notas)
soma = 0.0
for i in range(n_notas):
    soma += notas[1]

media = soma/n_notas
print(media)