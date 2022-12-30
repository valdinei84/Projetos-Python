# Crie uma função que, ao receber um número inteiro, retorna se um número é ár ou ímpar 
# (utilizando **Kwargs)
from unittest import result


def func(**kwargs):
    print(kwargs['par_impar'])
    
numero = int(input("Informe o primeiro número "))
result = numero % 2

if result == 0:
        par = (f'O número {numero} é par')
        func(par_impar = 'par')

else:
        impar = (f"O número {numero} é impar")

        func(par_impar = 'impar')
        

    
'''
numero = int(input('Me informe um número qualquer: '))
print (f"Voce digitou o úmero {numero}")
resultado = numero % 2
if resultado == 0:
    print (f'O número {numero} é par')
else:
    print (f"O numero {numero} é impar") 
'''