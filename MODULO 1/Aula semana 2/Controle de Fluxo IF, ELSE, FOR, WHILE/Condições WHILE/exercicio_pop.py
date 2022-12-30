a = ['Tomate', 'Arroz', 'Feijão']
while a != []:
    item = a.pop() #Esse pop serve para gegar sempre de traz pra frente.
    print(item)
    if a == []: # significa que se o a estver vazia mostre lista completa
        print("Lista Completa")
'''
['foo', 'bar', 'baz']
['foo', 'bar']
['foo']
[]
'''