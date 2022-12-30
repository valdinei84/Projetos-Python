# Crie uma função de somatório que some todos os números que a função receber (usando *args).
def somatorio(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma 
print(somatorio(10,9,5,6,3,4))
    