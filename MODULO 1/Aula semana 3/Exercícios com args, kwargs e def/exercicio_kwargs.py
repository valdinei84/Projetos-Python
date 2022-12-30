# kwargs são representados com dois asteristicos (**)
# adicionando um nome 
def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs['idade']
    print(f'tem 8{idade} anos')
lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Valdinei', sobrenome='Welter', idade=30)