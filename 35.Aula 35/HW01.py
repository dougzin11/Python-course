'''
Escreva uma função que obtenha a multiplicação de vários números de entrada
'''

def multiplica(*numeros):
    multiplicacao = 1
    for num in numeros:
        multiplicacao *= num
    return multiplicacao