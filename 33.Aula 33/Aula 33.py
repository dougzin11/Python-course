##### Aula 33 - Funções 1: Introdução, Valores de Retorno #####
'''
Escreve uma função de potenciação
'''

def potencia(base, exp):
    pot = base**exp

    return pot

print(potencia(2,3))

'''

'Faça um programa, com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos
'''

def soma(num1, num2, num3):
    return num1+num2+num3

print(soma(1,2,3))

'''
Escreva uma função que recebe dois números e devolve a soma e a 
multiplicação entre os dois
'''

def opMat(num1, num2):
    return num1+num2, num1*num2

a,b = opMat(2,3)
print(opMat(2,3))
print(a)
print(b)

'''
Escreva uma função que sorteie um lançamento de dado e imprima
o resultado
'''

import random
def lancaDado():
    a = random.randint(1,7)
    print(a)

lancaDado()