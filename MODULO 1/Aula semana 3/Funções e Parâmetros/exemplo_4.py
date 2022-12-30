valores = [1,2,3,4,5]

def quadrado (valores):
    quadrado = []
    for x in valores:
        quadrado.append(x**2) ## append se usa pra anexar valores
    return quadrado

resultados = quadrado(valores)

for y in resultados:
    print(y)
    
    