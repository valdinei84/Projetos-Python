# Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.

media_alunos = [] # Vai ser o locar onde vai armazenar a média dos alunos
alunos_acima_media = 0

for alunos in range(10):
#    alunos = ['José', 'Carlos', 'Jonas', 'Maria', 'Adair', 'Verônica', 'Gertrudes', 'Fredy', 'Matheus', 'Jéssica']
    soma_das_notas = 0 # significa que a soma das notas começa em 0 apos cada aluno separadamente
    # O segundo for serva para o programa pedir 4 x uma nota de cada um dos 10 alunos
    for nota in range(4):
        print("Digite a ", nota+1, "º nota do ", alunos+1, 'º aluno', sep="")
        soma_das_notas += float(input()) 
        
    media_alunos.append(soma_das_notas/4)
    
    if media_alunos[alunos] >= 7.0:
        alunos_acima_media += 1
        
    print("Médias dos alunos:", media_alunos)
    print("Números de alunos acima da média", alunos_acima_media)