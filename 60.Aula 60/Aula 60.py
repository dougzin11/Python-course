class Minha(object):
    def __init__(self):
        self.x = 0
        self.y = 0

meu = Minha()
# Acessar o valor de x e y
meu.x
meu.y


class Pessoa(object):
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()

class Cachorro(object):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def daApatinha(self):
        print("%s extendeu a patinha" % (self.nome))
    def latir(self):
        print("AU AU AU AU AU AU")

# Criar objeto rex
rex = Cachorro("Rex", "marrom")

# Criar objeto pessoa
pedro = Pessoa("Pedro", 75, rex)

# Podemos acessar o atributo cachorro
print(pedro.cao)

# Podemos acessar os atributos do cachorro
print(pedro.cao.cor)

# Treinar o cachorro
pedro.treinar()


## Funcao que recebe objetos
def MudaNome(pessoa):
    pessoa.nome = 'Lucas'

# Modificamos o nome do objeto pedro
MudaNome(pedro)
print(pedro.nome)