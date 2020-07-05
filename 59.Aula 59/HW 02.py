"""
Classe retângulo: crie uma classe que modele um retangulo

Atributos: lado A, lado B
Métodos: mudar valor dos lados, retornar valor dos lados, calcular área e calcular perímetro

Crie um programa que utilize esta classe. Ela deve pedir ao usuário que informe as medidas de um local. Depois, deve criar um objeto
com as medidas e calcular a quantidade de pisos necessários para o local

"""
# Importar biblioteca auxiliar
import math

# Criar o objeto
class retangulo(object):
    def __init__(self, comp_piso, larg_piso):
        self.comprimento = comp_piso
        self.largura = larg_piso
    def change_size(self, new_comp_piso, new_larg_piso):
        self.comprimento = new_comp_piso
        self.largura = new_larg_piso
    def print_size(self):
        print("Comprimento: %d" % (self.comprimento))
        print("Largura: %d" % (self.largura))
    def calc_area(self):
        area = self.comprimento * self.largura
        return area
    def calc_perim(self):
        perimetro = 2*self.comprimento + 2*self.largura
        return perimeto


comprimento = float(input("Informe o comprimento do local: "))
largura = float(input("Informe a largura do local: "))

largura_piso = float(input("Digite a largura do piso: "))
comprimento_piso = float(input("Digite o comprimento do piso: "))

piso = retangulo(comprimento_piso, largura_piso)

areaTotal = largura*comprimento
num_de_pisos = math.ceil(areaTotal / piso.calc_area())

print("Serão necessários %d número de pisos" % (num_de_pisos))