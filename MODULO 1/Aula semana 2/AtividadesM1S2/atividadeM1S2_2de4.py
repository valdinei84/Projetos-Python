'''
O caixa no bar do Sr. João está cheio de diversas moedas. 
O Sr. João precisa fechar o caixa, mas está com dificuldade de fazer os 
cálculos do tanto de dinheiro que ele possui em moedas. 
Enquanto estava organizando, ele conseguiu separar as moedas e contar a quantidade delas conforme a tabela:
Moeda	Quantidade
5 centavos	35
10 centavos	50
25 centavos	30
50 centavos	15
1 real	19
Crie uma aplicação que calcule o valor total que o Sr. João possui em moedas de real (R$) no caixa. 
A aplicação deve imprimir o valor total em reais (R$) e pode-se 
utilizar ponto flutuante para representar o valor com duas casas decimais no momento que for 
imprimir o valor na tela.
'''
centntavos5 = (0.05 * 5)
centavos10 = (0.10 * 50)
centavos25 = (0.25 * 30)
centavos50 = (0.50 * 15)
real = 19
total = float(centntavos5 + centavos10 + centavos25 + centavos50 + real)

print ('O tatal em moedas que o Senhor João possui é de', "%2f" % total, 'reais')