'''
Escreva uma função que obtenha o maior número de uma sequência de números
'''

def maior_num(*numeros):
    maior = numeros[0]
    for num in numeros:
        if num > maior:
            maior = num

    return maior