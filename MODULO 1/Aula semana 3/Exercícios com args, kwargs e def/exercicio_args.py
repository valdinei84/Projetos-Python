# Funções *args
# Para a função args e representada pelo * por padrão e usado *args porem pode ser por exemplo *casa,
# Exemplos:
#def func (*args):
#    print(args)
    
#lista = [1, 2, 3, 4, 5]
#n1, n2, *n = lista
#print(n1, n2, n) # o (n) ele ja automáticamente ja pega o restante da lista
#print(*lista)

# Segunda Parte dos ARGS
# Usando separador 

#def func(*args):
#    print(args)

#lista = [1,2,3,4,5]
#print(*lista, sep='_') # é apenas um separador pode ser usado qualquer outra coisa em vez de _

# Acessando eles de modo diferente mais simplificado
'''
def func(*args):
    print(args) 
    print(args[0]) # aqui vamos ver a linha inteira (tupla)
    print(args[-1]) # aqui ele vai mostrar o ultimo elemento
    print(len(args)) # serve para ver quantos argumentos tem dentro desse args (tamanho)
    
func(1,2,3,4,5)
'''
# Numa lista pdemos fazer algo similar
# Exemplo:
'''
def func(*args):
    args = list(args)
    args[0] = 20
    print(args)

func(1,2,3,4,5)
'''
# Mais uma função:
def func(*args):
    print(args)
    
lista = [1, 2, 3, 4, 5]
func(*lista, 10, 20, 30, 40, 50)
# neste caso aqui ele junta as duas listas