# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

Temperatura = float(input("Infore a temperatura do seu ambiente em Fahrenheit: "))
Celsius = (Temperatura - 32) / 1.8

print("A temperatura em Celsius é de ", Celsius)