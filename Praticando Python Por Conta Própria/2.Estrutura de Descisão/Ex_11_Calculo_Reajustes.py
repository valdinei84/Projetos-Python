'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

Salário_Atual = float(input("Digite seu salário atual: "))
if Salário_Atual <= 279:
    Salário_Atual20 = Salário_Atual * 0.2
    salario_soma = Salário_Atual20 + Salário_Atual
    print(f"Seu salário era de {Salário_Atual:.2f} teve um aumento de 20%, {Salário_Atual20:.2f}, e pasou a ser {salario_soma:.2f} R$")
elif Salário_Atual >= 280 and Salário_Atual <= 699:
    Salário_Atual15 = Salário_Atual * 0.15
    salario_soma = Salário_Atual15 + Salário_Atual
    print(f"Seu salário era de {Salário_Atual:.2f} teve um aumento de 15%, {Salário_Atual15:.2f}, e pasou a ser {salario_soma:.2f} R$")
elif Salário_Atual >= 700 and Salário_Atual <= 1499:
    Salário_Atual10 = Salário_Atual * 0.10
    salario_soma = Salário_Atual10 + Salário_Atual
    print(f"Seu salário era de {Salário_Atual:.2f} teve um aumento de 10%, {Salário_Atual10:.2f}, e pasou a ser {salario_soma:.2f} R$")
elif Salário_Atual >= 1500:
    Salário_Atual5 = Salário_Atual * 0.05
    salario_soma = Salário_Atual5 + Salário_Atual
    print(f"Seu salário era de {Salário_Atual:.2f} teve um aumento de 5%, {Salário_Atual5:.2f}, e pasou a ser {salario_soma:.2f} R$")

