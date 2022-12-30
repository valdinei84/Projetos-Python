# Exercício 4
# Faça um Programa que leia um vetor de 10 caracteres, 
# e diga quantas consoantes foram lidas. 
# Imprima as consoantes

verifica_consoantes = ['cArlos', 'casas', 'comida', 'gabriel', 'ricardo', 'olindo', 'hospital', 'cortina', 'parede', 'sanfona']
#print(verifica_consoantes)
consoante = 0

for words in verifica_consoantes:# Percorre cada palavra da lista
    consoante2 = 0
    words = words.lower() # Função que torna string em minusula . upper para maiúsculo
    for letter in words: # Percorre cada letra de cada palavra
        print(letter, end=" ")
        if letter not in ["a", "e", "i", "o", "u"]:# se a letra não é uma vogal, é consoante
            consoante = consoante + 1
            consoante2 = consoante2 + 1
    print(words)
    print(consoante2)
print(consoante)
