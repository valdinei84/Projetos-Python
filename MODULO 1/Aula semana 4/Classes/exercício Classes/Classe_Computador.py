# 1.0 Dando nome pra Classe:
# init (consultor) ele permite criar a funcionalidade inicial que uma classe terá
# o Self serve para definir propriendades e elementos dentro de uma instância
class Computador: 
# Adicionar pripriedades dentro da Classe
    def __init__(self, marca, memoria_ram, placa_de_video): 
# defenindo uma classe dinamicamente para que cada um recebe seu valor individualmente, depois do self
# neste momento os nomes apos o self acima dever ser colocados em cada um abaixo também
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

# Aqui vamos definir um método para ligar o computador com toda sua lógica
    def Ligar (self):
        print('Estou Ligando')
        
    def Desligar (self):
        print("Estou Desligando")
    
    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)
# neste parametro de Exibir ele vai mostrar as informações do computador que esta sendo desligado

# Criando uma instância da classe
computador1 = Computador("Asus","16gb","Nvidia")
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()

'''    pass #Acima e um modo mais simplificado

# Instanciar uma classe:
# devemos passar os valores para cada um individualmente
computador1 = Computador('Asus','8gb','Nvidea') 
computador2 = Computador('Dell','10gb','GeForce')
computador3 = Computador('Acer','16gb','ATM')
print('Computador 1 é um: ',computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print('Computador 2 é um: ',computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
print('Computador 3 é um: ',computador3.marca, computador3.memoria_ram, computador3.placa_de_video)
'''