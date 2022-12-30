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
valor = 100#(input('Valor do saque: '))
caixa_eletronico.sacar(valor)