'''Contando números páres'''
for numero in range (1000):
    if numero % 2 != 0:
        continue
    print (f'O número {numero} é par!')
    if numero == 20:
        print ('OPS... já verifiquei muitos números pares')
        break