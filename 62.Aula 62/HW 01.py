"""
Defina uma nova classe ObjetoGráfico subclasse de object, cujos atributos são:
    cor_de_preenximento --> inteiro
    preenxida --> bool
    cor_de_contorno --> inteiro

Escreva três classes:
    Retangulo --> Atributos: base e altura
    Circulo --> Atributos: raio
    Triangulo --> Atributos: base e altura

Subclasses da classe ObjetoGráfico que possuam todas métodos area e perimetro
"""

import math

class ObjetoGrafico(object):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno):
        self.cor_de_preenximento = int(cor_de_preenximento)
        self.preenxida = bool(preenxida)
        self.cor_de_contorno = int(cor_de_contorno)

class Retangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno, base, altura):
        super(Retangulo, self).__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura
    def perimetro(self):
        return self.base*2 + self.altura*2
    def area(self):
        return self.base*self.altura

class Circulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno, raio):
        super(Circulo, self).__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.raio = raio
    def perimetro(self):
        return 2*math.pi*self.raio
    def area(self):
        return math.pi*(self.raio)**2

class Triangulo(ObjetoGrafico):
    def __init__(self, cor_de_preenximento, preenxida, cor_de_contorno, base, altura):
        super(Triangulo, self).__init__(cor_de_preenximento, preenxida, cor_de_contorno)
        self.base = base
        self.altura = altura
    def perimetro(self):
        pass
    def area(self):
        return self.base*self.altura/2