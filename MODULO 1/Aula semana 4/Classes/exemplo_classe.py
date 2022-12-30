class Cachorro:
    def __init__(self, nome:str, raca:str, comprimeto:float, peso:float):
        self.nome = nome
        self.raca = raca
        self.comprimento = comprimeto
        self.peso = peso
        
    def latir(self):
        print(f'Au aul! Eu sou o(a) {self.nome}')
    
    def morder(self):
        print(f'O(a) cachorro(a) {self.nome} te mordeu!')
        
    def dormir(self):
        print('ZzZzZzZz...')
        
    def brincar(self):
        print('Eu gosto de brincar de bolinha!')
        
    def comer(self):
        print(f'Eu peso {self.peso} Kg e preciso comer {self.peso * 1000 * 0.01} g de comida para ficar satisfeito(a)!')
        
    