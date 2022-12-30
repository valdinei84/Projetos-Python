alunos = ['Elysson', 'Giulia', 'Pedro', 'Thiago', 'Vanessa']
alunos_presentes = 0

for aluno in alunos:
    print ('{} presente!'.format(aluno))
    alunos_presentes += 1

    print ('Quantidade de alunos presentes: {}'.format(alunos_presentes))