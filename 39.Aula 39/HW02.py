"""
Escreva uma função recursiva que retorna a soma de n até zero
"""

soma = 0

def SomaRecursiva(n):
    global soma
    if n > 0 and n != 0:
        soma += n
        SomaRecursiva(n-1)
    elif n < 0 and n!= 0:
        soma += n
        SomaRecursiva(n+1)
    else:
        print(soma)

SomaRecursiva(4)