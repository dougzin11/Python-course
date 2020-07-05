##### Aula 68 - Exceções 2: Raise e Excessões Próprias #####

# Exemplo 1
def teste():
    try:
        a = int(input('Escolha um número entre 1 e 20: '))
        if not 1 <= a <= 20:
            raise ValueError
        else:
            print(f'Você escolheu o número {a}')
    except ValueError:
        print('Entrada inválida')


# Exemplo 2
class ValorRepetidoErro(Exception):
    def __init__(self, n):
        self.num = n
    def __str__(self):
        return f'Você já digitou o número {self.num} antes'

def main():
    lista = []

    for i in range(3):
        while True:
            try:
                num = int(input('Escolher um número: '))
                break
            except ValueError:
                print('Digite apenas números!')

        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num)


if __name__ == '__main__':
    main()