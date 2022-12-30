#declaração return sendo utilizada ao fim da função para retornar um valor desejado.
numero = int(input("Informe um número "))
def par_impar(numero = numero %2):
    return numero 
if par_impar == 0:
    print(f"o numero {numero} é par")
else:
    print(f'O número {numero} é impar')