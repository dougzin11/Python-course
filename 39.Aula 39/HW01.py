"""
Escreva uma função recursiva que imprima de um número x até um y
"""

def imprimir(x, y):
    if x <= y:
        print(x)
        imprimir(x + 1,y)

imprimir(0, 10)