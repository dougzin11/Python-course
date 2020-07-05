'''
Classe pessoa: crie uma classe que modele uma pessoa

Atributos: nome, idade, peso e altura
Métodos: envelhecer, engordar, emagrescer e crescer

OBS: por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0.5 cm
'''

class pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, mais_idade = 0):
        i = 0
        while i != mais_idade:
            self.idade += 1
            if self.idade <= 21:
                self.altura += 0.5
            i += 1
        print (self.idade)
    def engordar(self, mais_peso = 0):
        self.peso += mais_peso
        print (self.peso)
    def emagrescer(self, menos_peso = 0):
        self.peso -= menos_peso
        print (self.peso)
    def crescer(self, mais_altura = 0):
        self.altura += mais_altura
        print (self.altura)

douglas = pessoa("Douglas", 15, 75, 169)
douglas.envelhecer()
douglas.envelhecer(1)
douglas.engordar(1)
douglas.emagrescer(1)
douglas.crescer(10)
douglas.envelhecer(5)
douglas.crescer()
douglas.envelhecer(5)
douglas.engordar(10)
douglas.emagrescer(20)