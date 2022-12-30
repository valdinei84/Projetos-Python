# args e kwargs
'''
def verificar (numero):
    if numero % 2 == 0:
        print("Numero é par!")
    else:
        print("Número é impar!")
verificar(2)
'''
def decorator(Function):
    def wrapper(*args, **kwargs):
        print("Antes da função")
    return wrapper

@decorator
def verificar(numero):
    if numero % 2 == 0:
        print("numero é par")
    else:
        print("Número é impar")
    
verificar(2)