class Meu_Objeto(object):
    def __init__(self, name, age = 0):
        self.nome = name
        self.idade = age
        print('Construtor chamado com sucesso')
    def imprime(self):
        print('Ola meu nome é %s e eu tenho %d anos'%(self.nome, self.idade))

hey = Meu_Objeto('Douglas', 27)
hey.imprime()