"""
Classe quadrado: crie uma classe que modele um quadrado

Atributos: tamanho do lado
Métodos: mudar valor do lado, retornar valor do lado e calcular área

"""

class quadrado(object):
    def __init__(self, size = 0):
        self.size = size
    def change_size(self, new_size):
        self.size = new_size
    def print_size(self):
        print("The square has size %d" % (self.size))
    def calculate_area(self):
        area = self.size**2
        print("The square has area %d" % (area))

square = quadrado(2)

# Testar métodos
square.print_size()
square.calculate_area()
square.change_size(3)
square.print_size()
square.calculate_area()