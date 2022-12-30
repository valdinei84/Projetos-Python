# Funções em (def) serve para definir uma função
# func seria a função para a definição dentro da def
# Entre os parenteces após a func são os argumentos 
def func (a1, a2, a3, a4, a5, nome=None, a6=None):
# Aqui ele imprime os argumentos    
    print(a1, a2, a3, a4, a5, nome, a6) 
# para chamar a função e dando valor ão a1, a2, a3, a4, e a5
# posso tambem nomear um argumento como por exemplo colocando nome,
# para isso acressentei uma variável na função como nome recebendo None,
# acrescentando a variável nome no print, e na func abixo colocando o nome dando o valor a ela, 
# nomeando a mesma como Luiz ou nome qualquer
# IMPORTANTE, a partir do momento que se seta um padrão em um argumento os demais também 
# devem seguir o mesmo padrão nos demais
#
# Para que minha variavel retorne algum valor de retorno eu preciso utilizar a palavra (return)
    return nome, a6 # nesse caso so ira retornar o que eu selecionei que no caso foi o valor do nome e do a6
# func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
var = func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
print(var)