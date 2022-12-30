#Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
letras = "Programando em Python"
numero_de_vezes = 0
for letter in letras : 
    if letter == "o":
        numero_de_vezes = numero_de_vezes + 1
print(numero_de_vezes)   
        
    