"""
Escreve um programa que recebe uma lista de números até que seja dada a entrada
-1, e depois imprima todos os números pares da sequência
"""

vetor =[]
num = int(input('Digite um numero: '))

while num != -1:
    vetor.append(num)
    num = int(input('Digite um numero: '))

for element in vetor:
    if element % 2 == 0:
        print(element)