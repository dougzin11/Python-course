"""

Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y
Possua uma classe chamada Retangulo, com os atributos largura e altura
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique
os valores de x e y para o centro do objeto

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo

"""

class Ponto(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def imprimir(self):
        print(self.x, self.y)

class Retangulo(object):
    def __init__(self, origin = Ponto(), largura = 0, altura = 0):
        self.largura = largura
        self.altura = altura
        self.origin = origin
    def centro(self):
        centro_x = self.origin.x + self.largura/2
        centro_y = self.origin.y + self.altura/2
        print(centro_x, centro_y)

def Menu():
    while True:
        command = str(input("Você deseja alterar os valores do retângulo (alterar), "
                        "imprimir o centro do retângulo (imprimir) ou sair do programa (sair)? ")).lower()
        if command not in ["alterar", "imprimir", "sair"]:
            print('Por favor digite uma resposta válida!')
        else:
            return command

def acao(command):
    if command == "alterar":
        input_origin_x = float(input("Digite a coordenada X da origem: "))
        input_origin_y = float(input("Digite a coordenada Y da origem: "))
        input_largura = float(input("Digite a largura do retangulo: "))
        input_altura = float(input("Digite a altura do retangulo: "))
        ponto = Ponto(input_origin_x, input_origin_y)
        retangulo = Retangulo(ponto, input_largura, input_altura)
        print('Valores alterados com sucesso!')
    elif command == "imprimir":
        return retangulo.centro()
    elif command == "sair":
        sair_loop = False
        return sair_loop

def main():
    ponto = Ponto()
    retangulo = Retangulo()
    print(retangulo)

    while True:
        user_input = Menu()
        if user_input == "alterar":
            input_origin_x = float(input("Digite a coordenada X da origem: "))
            input_origin_y = float(input("Digite a coordenada Y da origem: "))
            input_largura = float(input("Digite a largura do retangulo: "))
            input_altura = float(input("Digite a altura do retangulo: "))
            ponto.x = input_origin_x
            ponto.y = input_origin_y
            retangulo = Retangulo(ponto, input_largura, input_altura)
            print('Valores alterados com sucesso!')
        elif user_input == "imprimir":
            retangulo.centro()
        else:
            break


main()
