##### Aula 42 - Funções 9: Exercício Jogo Bagels #####
import random

ult_dig = (lambda x: x%10)

def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada é válida ou não,
    tendo em vista o número de dígitos
    True -> Entrada Válida
    False -> Entrada Inválida
    :param num: digitos
    :return: boolean
    """
    if num < 1000 or num >= 10000:
        return False
    else:
        return True

def GeraSecretNum():
    """
    Função que gera e retorna o número secreto
    E a lista contendo cada um de seus dígitos
    Ex:
    secretNum = 1783
    list_num = [1, 7, 8, 3]
    OBS: Numero não pode ter dígitos repetidos
    """
    numeros = list(range(10))
    secretNum = 0

    while numeros[0] == 0:
        random.shuffle(numeros)

    for i in range(4):
        dig = numeros[i]
        secretNum += dig*(10**(3-i))

    return secretNum, numeros[:4]

def GeraDicas(num, secretNum, secretNumList):
    '''
    Recebe o número escolhido e o número secreto e gera uma lista
    contendo as dicas a serem colocadas
    Código
    --> 0 = Bagels
    --> 1 = Pico
    --> 2 = Fermi

    123
    1783
    Retorna uma lista vazia caso os dois números sejam iguais
    '''
    global ult_dig

    if secretNum == num:
        return []

    dica = []

    for i in range(4):
        if ult_dig(num) == ult_dig(secretNum):
            # Fermi
            dica.append(2)
        elif ult_dig(num) in secretNumList:
            # Pico
            dica.append(1)

        num //= 10
        secretNum //= 10

    if len(dica) == 0:
        # Bagels
        dica.append(0)

    dica.sort()

    return dica