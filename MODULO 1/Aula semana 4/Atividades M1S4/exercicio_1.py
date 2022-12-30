'''
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico.

Os requisitos básicos são os seguintes:

Entregar o menor número de notas; 
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00 Exemplos:
Valor do Saque: R$ 30,00 - Resultado esperado: 
Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00. Valor do Saque: R$ 80,00 - 
Resultado esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
Referência: https://dojopuzzles.com/problems/caixa-eletronico/

Nossa sugestão é trabalhar em grupos ou em duplas.

Os tutores também estão disponíveis para quem precisar tirar dúvidas.
'''
'''
class CaixaEletronico:
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome
        
    def sacar(self, valor_saque):
        #começe aqui eu código
        restante = valor_saque
        
        notas_entregues = [0,0,0,0,0]
        i = 0
        while(restante > 0):
            nota_atual = self.notas[i]
            if nota_atual <= restante:
                restante -= nota_atual
                notas_entregues[i] += 1
            else:
                i += 1
        print(notas_entregues)
    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))
        
        
#if __name__=='__main__':
caixa_eletronico = CaixaEletronico("PD0922 Bank")
valor = int(input('Valor do saque: '))
caixa_eletronico.sacar(valor)
'''
class CaixaEletronico:
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome

    def sacar(self, valor_saque):
        valor = valor_saque
        resto = -1
        notas_entregues = []
        for valor_nota in self.notas:
            qtd_notas = valor // valor_nota
            resto = valor % valor_nota
            valor = resto
            if qtd_notas > 0:
                notas_entregues.append(f'{qtd_notas} nota de R$ {valor_nota},00')

        if resto == 0:
            self.imprimir_resultado(notas_entregues)
        else:
            print(f'Não é possível sacar o valor R$ {valor_saque},00')
    
    def imprimir_resultado(self, notas_entregues):
            print(', '.join(notas_entregues))

if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Ultima Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.sacar(valor)