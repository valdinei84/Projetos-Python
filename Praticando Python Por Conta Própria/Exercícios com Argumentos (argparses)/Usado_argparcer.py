# Fazer um programa que receba a largura e o compimento de um terreno e calcule a sua área
import argparse
# 1.0 Criando um objeto 
parser = argparse.ArgumentParser(description="Calcular a área de um terreno")
# 1.1 Adicionar os argumentos posicionais com o método add_argument():
parser.add_argument("largura", type=int, help="Largura do Terreno")
parser.add_argument("Comprimento", type=int, help="Comprimento do Terreno")
args = parser.parse_args()

# 1.2 Criando função para calcular a area
def calcula_area(largura, comprimento):
    area = largura * comprimento
    return area

# 1.3 Determinando a execução do projeto
if __name__=="__main__":
    print(f"A área do terreno é de {calcula_area(args.largura, args.comprimento)}")